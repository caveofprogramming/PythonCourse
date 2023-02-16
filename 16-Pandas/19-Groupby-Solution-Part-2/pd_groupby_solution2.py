import pandas as pd
import matplotlib.pyplot as plt

"""
Add an "age group" column to the mall customers dataset: young, middle and old.

Create scatter plots of income vs average spending, one for each age group.
"""

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    labels=['Young', 'Middle', 'Old']

    df['Age Group'] = pd.cut(df['Age'], 3, labels=labels)

    groups = df.groupby(['Age Group', 'Income'])['Spending'].mean().dropna()

    pd.set_option("display.max_rows", 200)

    fig = plt.figure()
    fig.suptitle("Income vs. Spending")

    for i, label in enumerate(labels):
        group = groups.loc[label]
        ax = fig.add_subplot(1, 3, i+1)
        ax.set_title(label)
        ax.set_xlabel('Income')
        ax.set_ylabel('Spending')
        ax.scatter(group.index, group.values)

    plt.show()

main()