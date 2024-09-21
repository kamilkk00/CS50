x = input("camelCase: ")
new_x = ""
for i in range(len(x)):
    if x[i].isupper():
        new_x += f"_{x[i].lower()}"
    else:
        new_x += x[i]
print(new_x)
