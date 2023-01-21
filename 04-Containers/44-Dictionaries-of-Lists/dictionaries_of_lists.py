
people = {
    "Al": ["Running", "Programming"],
    "Clare": ["Hiking", "Reading", "Skiing"],
}

print(people["Clare"][1])

for name, hobbies in people.items():
    print(name)
    print("=====")

    for hobby in hobbies:
        print(hobby)
    print()
