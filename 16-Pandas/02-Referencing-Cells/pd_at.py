#!./venv/bin/python

import pandas as pd

def main():
    df = pd.read_csv('exercises.csv', sep=',', index_col=0)
    df.columns = df.columns.str.strip()

    print(df.at['Wed', 'Pushups'])
    print(df.iat[3, 0])

    df.at['Wed', 'Pushups'] = 40

    print(df)
    

if __name__ == "__main__":  
    main()
