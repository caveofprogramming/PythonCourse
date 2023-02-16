#!./venv/bin/python

import pandas as pd

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


if __name__ == "__main__":  
    main()
