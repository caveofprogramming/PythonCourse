import re

result = re.match(r"([a-z][a-z\.\-]+)@(\w+)\.(\w+)", "john.purcell@caveofprogramming.com")

name, domain, suffix = result.groups()

print(name, domain, suffix)