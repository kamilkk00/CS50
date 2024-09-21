from datetime import date
import inflect, sys, re


def main():
    date_input = str(input("Date: "))
    b = into_word(date_input)
    print(b, "minutes")

def date_transformation(date_input):
    if match := re.search(r"^([0-9][0-9][0-9][0-9])-[0-9][0-9]-[0-9][0-9]$", date_input):
        x = date.fromisoformat(date_input)
        return x
    else:
        return sys.exit ("Invalid date")

def counting(ile):
    #today = date(2024, 6, 5)
    today = date.today()
    x = date_transformation(ile)
    o = (today - x).days
    z = o * 24 * 60
    return z

def into_word(data):
    a = counting(data)
    inflector = inflect.engine()
    words = inflector.number_to_words(a, andword = "").capitalize()
    return words


if __name__ == "__main__":
    main()
