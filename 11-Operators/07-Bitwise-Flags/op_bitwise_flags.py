#!./venv/bin/python

def printb(value):
    print(f"{value:08b}")

class Flags:
    LOUDER = L = 1
    DENOISE = N = 2
    DEESS = S = 4

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
