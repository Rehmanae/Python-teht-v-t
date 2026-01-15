# Ensin kysytään vanhat mitat
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Tämän jälkeen muutetaan kaikki luodeiksi
luodit_yht = leiviskat * 20 * 32 + naulat * 32 + luodit

# Siten luodit grammoiksi
grammat = luodit_yht * 13.3

# kokonaiset kilot ja loput grammat
kilot = int(grammat / 1000)
grammat_jaljella = grammat - kilot * 1000

# Lopuksi tehdään tulostus
print("Massa nykymittojen mukaan:")
print(str(kilot) + " kilogrammaa ja " + str(grammat_jaljella) + " grammaa.")
