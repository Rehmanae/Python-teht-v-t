# Ensin kysytään kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

# Sen jälkeen lasketaan summa, tulo ja keskiarvo
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# tulostetaan tulokset
print("Summa:", summa)
print("Tulo:", tulo)
print("Keskiarvo:", keskiarvo)