#!./venv/bin/python

import os

def main():
    #print(os.sep)
    #print(os.path.join('one', 'two', 'three', ''))
    #print(os.listdir())
    #print(os.path.exists('file_array.py'))

    for (root, dirs, files) in os.walk('games'):
        #print(root, dirs, files)

        for file in files:
            print(os.path.join(root, file))


   
if __name__ == "__main__":  
    main()
