#!./venv/bin/python

def main():
    months = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
    }

    months["Apr"] = "April"

    months.update({"May": "May", "Jun": "June"})

    print(months)

main()