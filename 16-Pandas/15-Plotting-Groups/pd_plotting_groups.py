#!./venv/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    gender_age_groups = df.groupby(['Gender', 'Age'])

    income = gender_age_groups['Income'].mean()

    print(df.groupby('Gender')['Income'].std())

    male = income.loc['Male']
    female = income.loc['Female']

    fig = plt.figure()
    ax = fig.add_subplot()

    fig.suptitle("Mall Customers Male vs Female Income")
    ax.scatter(male.index, male.values, color='blue')
    ax.scatter(female.index, female.values, color='red')
    ax.set_xlabel("Age")
    ax.set_ylabel("Income")


    plt.show()


if __name__ == "__main__":  
    main()
