import mysql.connector

# Yhteys tietokantaan
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="Rehman087565426.",
    autocommit=True
)
maakoodi = input("Anna maakoodi (esim FI): ").upper()

sql = """
SELECT type, COUNT(*) 
FROM airport
WHERE iso_country = %s
GROUP BY type
"""

kursori = yhteys.cursor()
kursori.execute(sql, (maakoodi,))
tulos = kursori.fetchall()

if kursori.rowcount > 0:
    for rivi in tulos:
        print(rivi[0], rivi[1])
else:
    print("Maakoodilla ei löytynyt lentoasemia.")