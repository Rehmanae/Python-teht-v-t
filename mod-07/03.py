# Tehtävä 3: lentoasemien tallennus ja haku

lentoasemat = {}

while True:
    print("\n1 - Lisää uusi lentoasema")
    print("2 - Hae lentoasema")
    print("3 - Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty.")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi on:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")