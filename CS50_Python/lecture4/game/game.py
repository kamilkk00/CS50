import random

number = random.randint(1, 100)
while True:
    try:
        b = int(input("Level: "))
        if b > 0:
            break
    except ValueError:
        p = 0
while True:
    try:
        a = int(input("Guess: "))
        if a >= 0:
            if a == number:
                print("Just right!")
                break
            elif a > number:
                print ("Too large!")
            elif a < number:
                print ("Too small!")
    except ValueError:
        p = 0
