import math

pienin = math.inf
suurin = -math.inf

syote = input("Anna luku: ")

while syote != "":
    luku = int(syote)

    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    syote = input("Anna luku: ")

# Tässä koodi laskee, kumpu luku on pienin ja suurin.
if pienin != math.inf:
    print(f"Pienin: {pienin}")
    print(f"Suurin: {suurin}")
else:
    print("Et antanut yhtään lukua")





