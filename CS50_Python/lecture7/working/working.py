import re

def main():
    x = convert(input("Hours: "))
    print (x)

def convert(s):
    x = s
    try:
        y = re.search(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", x, re.IGNORECASE)
        start_hour = int(y.group(1))
        start_minute = int(y.group(2)) if y.group(2) else 0
        start_period = y.group(3).upper()
        end_hour = int(y.group(4))
        end_minute = int(y.group(5)) if y.group(5) else 0
        end_period = y.group(6).upper()

        if start_period == "PM" and start_hour != 12:
            start_hour += 12
        elif start_period == "AM" and start_hour == 12:
            start_hour = 0

        if end_period == "PM" and end_hour != 12:
            end_hour += 12
        elif end_period == "AM" and end_hour == 12:
            end_hour = 0

        if start_minute >= 60 or end_minute >= 60:
            raise ValueError("Invalid minute value")

        start_time = f"{start_hour:02}:{start_minute:02}"
        end_time = f"{end_hour:02}:{end_minute:02}"
        return f"{start_time} to {end_time}"
    except AttributeError:
        raise ValueError


if __name__ == "__main__":
    main()
