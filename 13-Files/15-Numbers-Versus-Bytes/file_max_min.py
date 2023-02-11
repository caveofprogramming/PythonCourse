#!./venv/bin/python

"""
000 0
001 1
010 2
011 3
100 4
101 5
110 6
111 7
"""


def main():
   print(pow(2, 3) - 1)
   print(pow(2, 2) - 1)
   print()
   print(pow(2, 8) - 1)
   print(pow(2, 7) - 1)
   print()
   print(pow(2, 16) - 1)
   print(pow(2, 15) - 1)
   print()
   print(0xFF)
   print(0xFFFF)
   print()

   # 4 bytes    7 digits
   # 8 bytes    16 digits

   # 4 bytes 12.34567

if __name__ == "__main__":  
    main()
