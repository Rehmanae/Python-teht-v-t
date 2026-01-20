sukupuoli = input("Mikä on sinun biloginen sukupuoli: ")
hemoglobiiniarvo = float(input("Mikä on sinun hemoglobiiniarvo?: "))

sukupuoli == "nainen"
sukupuoli == "mies"

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen!")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali!")
    else:
        print("Hemoglobiiniarvo on korkea!")


if sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen!")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali!")
    else:
        print("Hemoglobiiniarvo on korkea!")

