# Ensimmäisenä kysytään mitat suorakulmion mitat.
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Sitten lasketaan pinta-ala ja piiri
pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

# Tämän jälkeen tulostetaan tulokset
print("Suorakulmion pinta-ala on:", pinta_ala)
print("Suorakulmion piiri on:", piiri)