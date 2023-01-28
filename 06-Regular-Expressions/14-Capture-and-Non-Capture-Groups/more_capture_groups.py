import re

email = "one.two.three.four@example.com"

result = re.match(r"((?:\w+\.)*)\w+@\w+\.\w+", email)

if result is None:
    print("No match")
else:
    print(result.group(0))
    print(result.groups())