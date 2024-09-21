def main():
    while True:
        fraction = str(input("x: "))
        if fraction == "0/100":
            print ("E")
            break
        else:
            try:
                c = gauge (fraction)
                if c == False:
                    z = 0
                else:
                    print (c)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid fraction.")
            except ZeroDivisionError:
                print("Invalid input. Division by zero is not allowed.")

def convert(fraction):
    try:
        x = fraction.split(sep="/")
        if len(x) != 2:
            raise ValueError("Invalid fraction format")
        a = int(x[0])
        b = int(x[1])
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return (a / b) * 100
    except ValueError:
        raise ValueError("Invalid fraction format")
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")

def gauge(percentage):
    try:
        percentage = int(percentage)
        if percentage == 0:
            return "E"
        elif percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        elif 1 < percentage < 99:
            return f"{percentage}%"
        else:
            return False
    except ValueError:
        return False
    except ZeroDivisionError:
        return False


if __name__ == "__main__":
    main()
