#!./venv/bin/python

import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    print(df.loc[(df['Gender'] == 'Female') & (df['Age'] == 32)])

    gender_age_groups = df.groupby(['Gender', 'Age'])

    for key in gender_age_groups.groups.keys():
        print(key)

    female_32 = gender_age_groups.get_group(('Female', 32))

    print(female_32)


if __name__ == "__main__":  
    main()
