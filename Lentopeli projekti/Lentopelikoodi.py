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