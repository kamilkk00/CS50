import random

def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level)
        a = random.randint(x, y)
        b = random.randint(x, y)
        for _ in range (3):
            correct_answer = a + b
            answer = int(input(f"{a} + {b} = "))
            if _ == 2 and answer != correct_answer:
                print ("EEE")
                print (f"{x} + {y} = {correct_answer}")
            if answer == correct_answer:
                score = score + 1
                break
            else:
                print("EEE")
    print ("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
        except ValueError:
            print("Must be Integor")

def generate_integer(level):
    if level == 1:
        x = 0
        y = 9
    elif level == 2:
        x = 10
        y = 99
    elif level == 3:
        x = 100
        y = 999
    return x, y


if __name__ == "__main__":
    main()
