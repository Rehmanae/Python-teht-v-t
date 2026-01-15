import random  # tuodaan random-kirjasto satunnaislukujen arpomiseen

# arvotaan kolmenumeroinen koodi yksitellen (0..9)
numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)
koodi3 = str(numero1) + str(numero2) + str(numero3)

# arvotaan nelinumerooinen koodi yksitellen (1..6)
numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)
koodi4 = str(numero4) + str(numero5) + str(numero6) + str(numero7)

# tulostus
print("Kolmenumeroinen koodi:", koodi3)
print("Nelinumerooinen koodi:", koodi4)
