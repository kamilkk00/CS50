def main ():
    time = str(input("What time is it? "))
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    y = float(hours)
    converted_time = y + x
    return converted_time

if __name__ == "__main__":
    main()
