def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

# pääohjelma
luvut = [9, 3, 4, 20]

tulos = laske_summa(luvut)
print("Listan summa on:", tulos)