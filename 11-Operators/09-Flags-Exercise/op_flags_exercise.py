#!./venv/bin/python

"""
Write a function which accepts a "flags" argument.

The flags will correspond to audio processing algorithms.

For each flag that is set when the function is called, print an 
appropriate message

For example:

process_audio(Flags.L|Flags.S)

prints:

Making louder ...
De-essing ...

Use the bitwise & operator to do this.

Next, if you haven't already done this, refactor your program so that
it makes use of a dictionary containing flags and their corresponding
text. Use a loop together with the dictionary to process the flags.
"""

def printb(value):
    print(f"{value:08b}")

class Flags:
    LOUDER = L = 1
    DENOISE = N = 2
    DEESS = S = 4
    NORMALIZE = O = 8
    REMOVECLICKS = R = 16

def main():

   printb(Flags.L)
   printb(Flags.N)
   printb(Flags.S)

   combined_flags1 = Flags.L | Flags.S
   printb(combined_flags1)

   combined_flags1 |= Flags.L
   printb(combined_flags1)

   combined_flags1 |= Flags.N
   printb(combined_flags1)

if __name__ == "__main__":  
    main()
