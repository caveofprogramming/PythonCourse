import pandas as pd
import matplotlib.pyplot as plt

def plot(df):
    fig = plt.figure(figsize=(16,9))
    ax = fig.add_subplot()
    ax.scatter(df['income'], df['spending'])
    ax.set_xlabel('Income')
    ax.set_ylabel('Spending')
    plt.show()

def main():
    df = pd.read_csv('mall_customers.csv')
    df.columns = ['id', 'gender', 'age', 'income', 'spending']

    plot(df)

main()