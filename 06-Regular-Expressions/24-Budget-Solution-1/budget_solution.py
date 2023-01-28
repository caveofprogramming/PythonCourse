#!./venv/bin/python

import re

data = """
Day         Electricity     Coffee      Cleaning
Monday      330             10          50
Tuesday     220             12          40
Wednesday   130             14          80
"""

lines = re.split("\n", data)

header = None

for line in lines:

    if re.search(r"^\s*$", line):
        continue

    fields = re.split("\s+", line)

    if header is None:
        header = fields
        continue

    print(fields)

print(header)