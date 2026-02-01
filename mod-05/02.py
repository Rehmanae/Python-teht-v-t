luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    # muutetaan syöte kokonaisluvuksi ja lisätään listaan
    luku = int(syote)
    luvut.append(luku)

# järjestetään luvut suurimmasta pienimpään
luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)