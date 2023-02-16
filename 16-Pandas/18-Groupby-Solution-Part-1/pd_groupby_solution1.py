import pandas as pd

"""
Add an "age group" column to the mall customers dataset: young, middle and old.

Create scatter plots of income vs average spending, one for each age group.
"""

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    df['Age Group'] = pd.cut(df['Age'], 3, labels=['Young', 'Middle', 'Old'])

    groups = df.groupby(['Age Group', 'Income'])['Spending'].mean().dropna()

    pd.set_option("display.max_rows", 200)

    print(groups)

main()