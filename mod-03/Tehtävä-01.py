# Kysytään kuhan pituus senttimetreinä
kuha = float(input("Mikä on kuhan pituus:"))

pituus = 37-kuha
if kuha >= 37:
    print("Voit pitää kuhan!")
else:
    print("Kuha on alimittainen se pitää heittää takaisin! " + str(pituus)+ "cm vähimmäispituus on 37cm")

