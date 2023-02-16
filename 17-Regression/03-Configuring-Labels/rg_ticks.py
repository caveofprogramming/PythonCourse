#!./venv/bin/python

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("weights.csv", index_col=0, sep='\s+')

    major_ticks = range(0, len(df.index), 7)
    labels = [df.index[x] for x in major_ticks]
    
    fig = plt.figure(figsize=(16,9))
    ax = fig.add_subplot()
    ax.set_xticks(ticks=major_ticks, labels=labels, rotation='vertical', minor=False)
    ax.set_xticks(ticks=range(len(df.index)),minor=True)
    ax.tick_params(axis='x', which='major', labelsize=10)
    ax.tick_params(axis='x', which='minor', labelsize=4)
    fig.suptitle("Weight vs Time")
    ax.grid()
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight(Kg)")
    ax.plot(df.index, df['weight'])
    plt.show()

if __name__ == "__main__":  
    main()
