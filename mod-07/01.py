# Moduuli 7 tehtävä 1 : kysytään kuukauden numero ja koodi tulosta vuodenaika.

vuodenajat = (
    "talvi",   # tammikuu
    "talvi",   # helmikuu
    "kevät",   # maaliskuu
    "kevät",   # huhtikuu
    "kevät",   # toukokuu
    "kesä",    # kesäkuu
    "kesä",    # heinäkuu
    "kesä",    # elokuu
    "syksy",   # syyskuu
    "syksy",   # lokakuu
    "syksy",   # marraskuu
    "talvi"    # joulukuu
)

kk = int(input("Anna kuukauden numero: "))

if kk >= 1 and kk <= 12:
    print("Vuodenaika on", vuodenajat[kk - 1])
else:
    print("Virheellinen kuukauden numero")