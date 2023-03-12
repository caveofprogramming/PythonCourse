#!./venv/bin/python

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("weights.csv", index_col=0, sep='\s+')

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle("Weight vs Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight(Kg)")
    ax.plot(df.index, df['weight'])
    plt.show()

if __name__ == "__main__":  
    main()

