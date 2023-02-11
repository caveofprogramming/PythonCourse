#!./venv/bin/python

import numpy as np
import re

data1 = """
            Water   Coffee   Tea (Litres)
Week1       50      60      45
Week2       100     150     180
Week3       70      50      45
Week4       45      20      15
"""

data2 = """
            Price per Liter
Water       0.2
Coffee      0.4
Tea         0.3
"""

"""
1. How much of each beverage was drunk in total?
2. How much liquid in total was consumed per week?
3. How much money was spent on beverages in each week?
4. How much money was spent in total on beverages?
"""

def load(data):

    result = []

    for line in data.split("\n"):
        matches = re.findall(r'\s+([\d\.]+)', line)

        if len(matches) > 0:
            result.append(matches)

    return result

def main():
    m1 = load(data1)
    m2 = load(data2)

    a1 = np.array(m1, dtype=float)
    a2 = np.array(m2, dtype=float)

    print(a1.sum(axis=0))    
    print(a1.sum(axis=1)) 

    print(np.matmul(a1, a2)) 

    print(np.matmul(a1, a2).sum(axis=0))  

if __name__ == "__main__":  
    main()
