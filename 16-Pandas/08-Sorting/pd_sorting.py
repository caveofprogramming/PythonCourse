#!./venv/bin/python

import pandas as pd

def main():
    df = pd.read_csv("mall_customers.csv", index_col= 0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    pd.set_option("display.max_rows", 10)

    df.sort_values(by=['Gender', 'Age'], inplace=True, axis=0, ascending=False)

    print(df)

if __name__ == "__main__":  
    main()
