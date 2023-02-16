#!./venv/bin/python

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.DataFrame([[1, 2, 3], [2, 3, 4], [5, 3, 3]], 
        columns=['cow', 'goat', 'sheep'],
        index=['grass', 'grain', 'hay'])

    print(df)
    print()
    for func in ['min', 'max', 'std', 'var', 'mean', 'sum']:
        f = getattr(df, func)
        print(func.title())
        print(f(axis=0))
        print()

    fig = plt.figure(figsize=(16,9))
    fig.suptitle("Animal Feed")

    for i, animal in enumerate(df.columns):
        ax = fig.add_subplot(1, 3, i+1)
        ax.set_title(animal.title())
        ax.pie(df.iloc[:,i], autopct='%.1f %%', labels=df.columns)

    plt.show()

if __name__ == "__main__":  
    main()
