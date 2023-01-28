"""
\w: Matches alphanumeric characters
+: matches one or more, as many as possible
\s: match a space
\d: digits
"""

import re

text = "The temperature is: 37"

result = re.match(r".*:\s*(\d+)", text)

print("No match" if result is None else f"'{result.group(1)}'")

