import inflect

list = [
]
p = inflect.engine()
a = True
try:
    while a == True:
        x = input ("Name: ")
        if x == "":
            break
        else:
            list.append(x)
except EOFError:
    print()
y = p.join((list))
print(f"Adieu, adieu, to {y}")
