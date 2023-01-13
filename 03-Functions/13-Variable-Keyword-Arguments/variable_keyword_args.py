
def add_description(**description):
    
    for prop in description:
        print(prop, ": ", description[prop])

    print()

def main():
    add_description(height=180, weight=90, eyes="blue")
    add_description(trousers="black", beard=True)
    add_description(sex="male", height=170)

main()