#!/usr/bin/env python3
"""Fix HSP — gen already wrote 80 to file via exec. Just verify."""
import json

# The gen_hsp exec in patch_remaining.py already wrote 80 questions
# (the 74 original + the 6 from patch) BUT then we added 6 more on top.
# Just truncate back to 80.
with open("/Users/user/personal/sb/trueassess/priv/question_bank/highly_sensitive.json") as f:
    hsp = json.load(f)

# Keep only first 80
hsp = hsp[:80]

# Re-assign UIDs to ensure uniqueness
for i, q in enumerate(hsp):
    q["uid"] = f"HSP-{i+1:03d}"

assert len(hsp) == 80
with open("/Users/user/personal/sb/trueassess/priv/question_bank/highly_sensitive.json", "w") as f:
    json.dump(hsp, f, indent=2)
print(f"HSP fixed: {len(hsp)} questions")
