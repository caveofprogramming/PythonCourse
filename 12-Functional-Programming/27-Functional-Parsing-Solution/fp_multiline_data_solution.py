#!./venv/bin/python

data = """
Day         Electricity     Coffee      Cleaning
Monday      330             10          50
Tuesday     220             12          40
Wednesday   130             14          80
"""

def main():
    for li in filter(lambda l: len(l) > 0, map(lambda s: s.split(), data.split("\n"))):
        print(li)

main()
