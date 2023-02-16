#!./venv/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

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

    x = np.arange(len(df.index))

    X = sm.add_constant(x)
    y_actual = df['weight']
    model = sm.OLS(y_actual, X)
    result = model.fit()

    intercept = result.params[0]
    gradient = result.params[1]
    y_predicted = intercept + gradient * x

    ax.plot(df.index, y_actual)
    ax.plot(x, y_predicted)
    #plt.show()

    print(result.summary())

    sum_square_residuals = np.sum((y_predicted - y_actual)**2)
    total_sum_square = np.sum((y_actual - np.mean(y_actual))**2)

    print(sum_square_residuals)
    print(total_sum_square)

    print(1 - sum_square_residuals/total_sum_square)

if __name__ == "__main__":  
    main()
