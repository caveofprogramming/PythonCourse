#!./venv/bin/python

import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    gp = df.groupby(by='Gender')

    print(type(gp))
    print(gp.ngroups)
    print(gp.groups)
    print(gp.groups.keys())
    pd.set_option("display.max_rows", 200)
    print(gp.get_group('Female'))
    print(gp.get_group('Male'))



if __name__ == "__main__":  
    main()
