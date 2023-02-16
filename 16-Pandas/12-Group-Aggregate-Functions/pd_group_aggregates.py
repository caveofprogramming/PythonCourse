#!./venv/bin/python

import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    gp = df.groupby('Gender')

    print(type(gp))

    male_dataframe = gp.get_group('Male')
    print(type(male_dataframe))

    male_income_series = male_dataframe['Income']
    print(type(male_income_series))

    grouped_income_series = gp['Income']
    print(type(grouped_income_series))

    print(gp.mean())
    print()
    print(grouped_income_series.mean())
    print()
    print(gp.agg([np.std, np.mean, len]))
    print()
    print(grouped_income_series.agg([np.std, np.mean, len]))

if __name__ == "__main__":  
    main()
