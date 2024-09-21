lista = {}
x = True
liczba = 1
z = 0
klucz = 0
try:
    while x == True:
        b = input("").upper()
        if b == "":
            break
        if b in lista:
            liczba = lista[b]
            liczba = liczba + 1
            lista [b] = liczba
        else:
            liczba = 1
            lista [b] = liczba

except EOFError:
    x = 0
myKeys = list(lista.keys())
myKeys.sort()
sorted_dict = {i: lista[i] for i in myKeys}
for key in sorted_dict:
   print (sorted_dict[key], key)
