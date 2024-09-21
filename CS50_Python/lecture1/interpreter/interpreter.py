expression = str(input ("Expression: " ))
x, y, z = expression.split(" ")

match y:
    case "+":
        o = float (x) + float (z)
    case "-":
        o = float (x) - float (z)
    case "/":
        o = float (x) / float (z)
    case "*":
        o = float (x) * float (z)
print (f"{o}")
