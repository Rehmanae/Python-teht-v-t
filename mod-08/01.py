import mysql.connector

# Yhteys tietokantaan
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="perususer",
    password="salainen",
    autocommit=True
)

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = "SELECT name, municipality FROM airport WHERE ident = %s"

kursori = yhteys.cursor()
kursori.execute(sql, (icao,))

tulos = kursori.fetchall()

if kursori.rowcount > 0:
    for rivi in tulos:
        print("Lentoaseman nimi:", rivi[0])
        print("Sijaintikunta:", rivi[1])
else:
    print("Lentoasemaa ei löytynyt.")