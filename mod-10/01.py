class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen = alin_kerros

    def ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print("Mennään ylös -> kerros", self.nykyinen)

    def alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print("Mennään alas -> kerros", self.nykyinen)

    def mene(self, kohde):
        while self.nykyinen != kohde:
            if self.nykyinen < kohde:
                self.ylos()
            else:
                self.alas()


# testaus
hissi = Hissi(1, 10)
hissi.mene(6)
hissi.mene(1)