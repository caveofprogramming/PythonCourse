#!./venv/bin/python

import re
from collections import defaultdict

data = """
Day         Electricity     Coffee      Cleaning
Monday      330             10          50
Tuesday     220             12          40
Wednesday   130             14          80
"""

category = defaultdict(float)
days = defaultdict(float)

lines = re.split("\n", data)

header = None

for line in lines:

    if re.search(r"^\s*$", line):
        continue

    fields = re.split("\s+", line)

    if header is None:
        header = fields
        continue

    day = fields.pop(0)

    for i, field in enumerate(fields):
        heading = header[i + 1]
        days[day] += float(field)
        category[heading] += float(field)

print(header)

print(days)
print(category)