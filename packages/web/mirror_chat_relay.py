"""
Mirror Chat Relay — Live session posting to iMessage group chat.

Reads the session JSONL transcript, extracts new messages, and posts them
to the "mirror chat" iMessage group with [mirror] or [bryan] prefixes.

Idempotent: tracks last posted position. Safe to restart.

Usage:
    python3 mirror_chat_relay.py              # run once (catch up + post new)
    python3 mirror_chat_relay.py --watch      # continuous: check every 60 seconds
    python3 mirror_chat_relay.py --watch 30   # continuous: check every 30 seconds
"""

import json
import subprocess
import sys
import time
import hashlib
from pathlib import Path
from datetime import datetime

# Configuration
TRANSCRIPT_FILE = Path("/Users/user/.claude/projects/-Users-user-personal-sb-pp/2ca0f748-943d-454f-a343-5f7282e58366.jsonl")
STATE_FILE = Path("/Users/user/personal/sb/pp/.mirror_chat_relay_state.json")
CHAT_NAME = "mirror chat"
MAX_MESSAGE_LENGTH = 2000  # iMessage has limits; chunk longer messages


def load_state():
    """Load relay state — tracks last posted position."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except:
            pass
    return {"last_line": 0, "last_hash": "", "messages_sent": 0}


def save_state(state):
    """Atomic save of relay state."""
    tmp = STATE_FILE.with_suffix('.tmp')
    tmp.write_text(json.dumps(state, indent=2))
    tmp.rename(STATE_FILE)


def send_imessage(text, chat_name=CHAT_NAME):
    """Send a message to an iMessage group chat via AppleScript."""
    # Escape for AppleScript
    escaped = text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

    # Truncate if needed
    if len(escaped) > MAX_MESSAGE_LENGTH:
        escaped = escaped[:MAX_MESSAGE_LENGTH - 20] + "... [truncated]"

    script = f'''
tell application "Messages"
    set targetChat to chat "{chat_name}"
    send "{escaped}" to targetChat
end tell
'''
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except Exception as e:
        print(f"  Send failed: {e}")
        return False


def extract_messages_from_line(line):
    """Extract displayable messages from a JSONL line."""
    try:
        msg = json.loads(line)
    except:
        return []

    message = msg.get('message', {})
    if not isinstance(message, dict):
        return []

    role = message.get('role', '')
    content = message.get('content', '')

    text = ''
    if isinstance(content, str):
        text = content
    elif isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get('type') == 'text':
                text += block.get('text', '') + '\n'
            elif isinstance(block, str):
                text += block + '\n'

    text = text.strip()

    # Skip empty, system messages, tool results, very short
    if not text or len(text) < 10:
        return []

    # Skip system reminders and hooks
    if text.startswith('<') or text.startswith('{'):
        return []

    # Skip tool call outputs that look like code/data
    if text.startswith('```') or text.startswith('def ') or text.startswith('import '):
        return []

    results = []
    if role == 'user':
        # Skip if it looks like a command or system message
        if text.startswith('/') or text.startswith('<'):
            return []
        results.append(f"[bryan] {text}")
    elif role == 'assistant':
        # Skip very technical responses (tool calls, code, etc.)
        if text.startswith('```') or 'python3' in text[:50]:
            return []
        results.append(f"[mirror] {text}")

    return results


def run_relay(watch=False, interval=60):
    """Run the relay — catch up and optionally watch for new messages."""
    state = load_state()
    print(f"Mirror Chat Relay started. Last position: line {state['last_line']}, {state['messages_sent']} messages sent.")

    while True:
        if not TRANSCRIPT_FILE.exists():
            print(f"Transcript not found: {TRANSCRIPT_FILE}")
            if not watch:
                break
            time.sleep(interval)
            continue

        # Read new lines since last position
        new_messages = []
        current_line = 0

        with open(TRANSCRIPT_FILE, 'r') as f:
            for i, line in enumerate(f):
                current_line = i + 1
                if current_line <= state['last_line']:
                    continue

                messages = extract_messages_from_line(line.strip())
                for msg in messages:
                    new_messages.append((current_line, msg))

        if new_messages:
            print(f"  {len(new_messages)} new messages to relay...")

            for line_num, msg in new_messages:
                # Chunk long messages
                if len(msg) > MAX_MESSAGE_LENGTH:
                    prefix = msg[:9]  # [bryan] or [mirror]
                    body = msg[9:]
                    chunks = [body[i:i+MAX_MESSAGE_LENGTH-20] for i in range(0, len(body), MAX_MESSAGE_LENGTH-20)]
                    for j, chunk in enumerate(chunks):
                        chunk_msg = f"{prefix} {chunk}"
                        if j < len(chunks) - 1:
                            chunk_msg += " ..."
                        if send_imessage(chunk_msg):
                            state['messages_sent'] += 1
                        time.sleep(0.5)
                else:
                    if send_imessage(msg):
                        state['messages_sent'] += 1

                state['last_line'] = line_num
                time.sleep(0.3)  # Don't flood

            save_state(state)
            print(f"  Relayed. Total sent: {state['messages_sent']}. Position: line {state['last_line']}.")
        else:
            if watch:
                pass  # Silent when no new messages in watch mode

        if not watch:
            break

        time.sleep(interval)


if __name__ == '__main__':
    watch = '--watch' in sys.argv
    interval = 60

    # Check for custom interval
    for i, arg in enumerate(sys.argv):
        if arg == '--watch' and i + 1 < len(sys.argv):
            try:
                interval = int(sys.argv[i + 1])
            except ValueError:
                pass

    # Option to start from current position (don't replay history)
    if '--from-now' in sys.argv:
        state = load_state()
        # Count total lines
        with open(TRANSCRIPT_FILE, 'r') as f:
            total = sum(1 for _ in f)
        state['last_line'] = total
        save_state(state)
        print(f"Set position to current end: line {total}. Will only relay NEW messages.")

    run_relay(watch=watch, interval=interval)
