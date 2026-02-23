import mysql.connector
from geopy.distance import geodesic

# Yhteys tietokantaan
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="perususer",
    password="salainen",
    autocommit=True
)

# Kysytään kaksi ICAO-koodia
icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

kursori = yhteys.cursor()

# Haetaan ensimmäisen kentän koordinaatit
kursori.execute(sql, (icao1,))
tulos1 = kursori.fetchone()

# Haetaan toisen kentän koordinaatit
kursori.execute(sql, (icao2,))
tulos2 = kursori.fetchone()

if tulos1 and tulos2:
    koord1 = (tulos1[0], tulos1[1])
    koord2 = (tulos2[0], tulos2[1])

    etaisyys = geodesic(koord1, koord2).kilometers

    print("Lentokenttien välinen etäisyys on", round(etaisyys, 2), "km")
else:
    print("Toista ICAO-koodeista ei löytynyt.")