import itertools

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

elements = list(alfabeto)

NumeroLettere = 3
combinations = itertools.product(elements, repeat=NumeroLettere)

stringa = ""

# Stampa delle stringhe
for c in combinations:
    stringa += "".join(c) + "\n"

f = open("password.txt", "w")
f.write(str(stringa))
f.close()
