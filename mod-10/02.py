"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron
 ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
"""

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin

    def ylos(self):
        if self.sijainti < self.ylin:
            self.sijainti += 1
            print("Hissi kerroksessa", self.sijainti)

    def alas(self):
        if self.sijainti > self.alin:
            self.sijainti -= 1
            print("Hissi kerroksessa", self.sijainti)

    def liiku(self, kohde):
        while self.sijainti < kohde:
            self.ylos()
        while self.sijainti > kohde:
            self.alas()


class Talo:
    def __init__(self, alin, ylin, maara):
        self.hissilista = []

        for nro in range(maara):
            uusi_hissi = Hissi(alin, ylin)
            self.hissilista.append(uusi_hissi)

    def kayta_hissia(self, numero, kohde):
        valittu = self.hissilista[numero]
        print(f"\nKäytetään hissiä {numero}")
        valittu.liiku(kohde)


# Tässä alkaa pääohjelma
talo = Talo(1, 8, 2)

talo.kayta_hissia(0, 5)
talo.kayta_hissia(1, 3)