#!./venv/bin/python

def describe_person(name, *attributes):
    print(name)

    for attribute in attributes:
        print(attribute)


def main():
    describe_person("Gizelle Loco", "warm", "depressive", "acerbic", "funny")
    print()
    describe_person("Giffy Mcbeth")
    print()
    describe_person("Spiff Lebiff", "whacky")

main()
