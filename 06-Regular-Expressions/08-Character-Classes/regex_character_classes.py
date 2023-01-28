import re

print(re.match(r"[a-z\d\-\.]+", "a-b.c3d"))

print(re.match(r"", "john.purcell@caveofprogramming.com"))