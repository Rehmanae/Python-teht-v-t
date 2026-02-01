import random

def heita_noppaa(tahkot):
    # palauttaa luvun 1..tahkot
    return random.randint(1, tahkot)

# pääohjelma
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

silmaluku = 0

while silmaluku != tahkojen_maara:
    silmaluku = heita_noppaa(tahkojen_maara)
    print("Silmäluku:", silmaluku)