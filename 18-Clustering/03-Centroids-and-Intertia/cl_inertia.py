import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot(df):
    fig = plt.figure(figsize=(16,9))
    ax = fig.add_subplot()
    ax.scatter(df['income'], df['spending'], c=df['cluster'], cmap='plasma')
    ax.set_xlabel('Income')
    ax.set_ylabel('Spending')

    means = df.groupby(by='cluster').mean()

    ax.scatter(means['income'], means['spending'], color='red', s=100)

    plt.show()

def cluster(df, n):
    X = df[['income', 'spending']]
    model = KMeans(n_clusters=n)
    model.fit(X)
    df['cluster'] = model.labels_

def main():
    df = pd.read_csv('mall_customers.csv')
    df.columns = ['id', 'gender', 'age', 'income', 'spending']

    cluster(df, 5)
    plot(df)

main()