#!./venv/bin/python

import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    values = np.random.randint(low=0, high=100, size=100)
    print(values[values < 48])
    print(values[(values == 48) | (values == 44)])

    print(df.loc[(df['Gender'] == 'Female') & (df['Age'] == 32)])


if __name__ == "__main__":  
    main()
