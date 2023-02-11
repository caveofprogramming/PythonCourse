#!./venv/bin/python

class Database():
    def __str__(self):
        return "database."

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, value, type, traceback):
        print(f"{value}, {type}, {traceback}")
        print("Exit")

def main():
    with Database() as db:
        print(db)
        raise Exception("Big problem!")

if __name__ == "__main__":  
    main()
