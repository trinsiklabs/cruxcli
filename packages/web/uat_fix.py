import re
with open('/Users/user/personal/sb/trueassess/test/uat/admin_uat_pass3.mjs') as f:
    content = f.read()
# Replace the broken eval section
content = content.replace(
    """const bodyText = await page.textContent('body') || ''; const ticketMatches = (bodyText.match(/TA-\\d{4}/g) || []).length; if (false) {
      // replaced
    }""",
    """const bodyText = await page.textContent('body') || '';
    const ticketMatches = (bodyText.match(/TA-\\d{4}/g) || []).length;"""
)
with open('/Users/user/personal/sb/trueassess/test/uat/admin_uat_pass3.mjs', 'w') as f:
    f.write(content)
print("Fixed")
