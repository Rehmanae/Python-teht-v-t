import random

lukumäärä = int(input("Kuinka monta noppaa?: "))

summa = 0
for nopan_nro in range(lukumäärä):
    silmaluku = random.randint(1, 6)
    print(f"noppa {nopan_nro + 1}, tulos = {silmaluku}")
    summa += silmaluku
print(f"silmälukujen summa = {summa}")
