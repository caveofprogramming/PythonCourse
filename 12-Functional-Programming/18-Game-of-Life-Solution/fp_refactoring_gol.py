for rowoffs in range(-1, 2):
    for coloffs in range(-1, 2):
        if rowoffs == 0 and coloffs == 0:
            continue

        print(rowoffs, coloffs)

print()

gen = ((rowoffs, coloffs) 
       for rowoffs in range(-1, 2) for coloffs in range(-1, 2) 
       if not (rowoffs == 0 and coloffs == 0))

for rowoffs, coloffs in gen:
    print(rowoffs, coloffs)
