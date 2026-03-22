"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

"""

import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus += muutos

        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunnit


# 🔹 Luodaan autot listaan
autot = []

for i in range(1, 11):
    rekisteri = "ABC-" + str(i)
    huippu = random.randint(100, 200)
    auto = Auto(rekisteri, huippu)
    autot.append(auto)


# 🔹 Kilpailu alkaa
kisa_ohi = False

while not kisa_ohi:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kisa_ohi = True


# 🔹 Tulostetaan
print("Rekisteri | Huippunopeus | Nopeus | Matka")
print("------------------------------------------")

for auto in autot:
    print(f"{auto.rekisteritunnus:10} {auto.huippunopeus:14} {auto.tamanhetkinen_nopeus:8} {auto.kuljettu_matka:10.1f}")