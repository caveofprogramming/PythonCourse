"""
\w: Matches alphanumeric characters
+: matches one or more, as many as possible
\s: match a space
\d: digits
"""

import re

text = "The temperature is 37."
text = "The price is 400."

result = re.match(r"\w+\s\w+\s\w+\s\d+\.", text)

print("No match" if result is None else f"'{result.group()}'")

