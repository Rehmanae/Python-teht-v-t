import requests

# kysytään käyttäjältä kaupungin nimi
kaupunki = input("Anna paikkakunta: ")

# tähän oma OpenWeather API-avain
api_key = "7db03310d2fbcf580e7eed62649734ea"

# tehdään osoite, josta haetaan sää
url = "https://api.openweathermap.org/data/2.5/weather?q=" + kaupunki + "&appid=" + api_key

# haetaan tiedot netistä
vastaus = requests.get(url)
data = vastaus.json()

# tarkistetaan onnistuiko haku (200 = ok)
if data.get("cod") == 200:
    # sääkuvaus
    kuvaus = data["weather"][0]["description"]

    # lämpötila kelvin-yksikössä
    lampotila_k = data["main"]["temp"]

    # muutetaan kelvinistä celsiukseksi
    lampotila_c = lampotila_k - 273.15

    print("Sää:", kuvaus)
    print("Lämpötila:", round(lampotila_c, 1), "C")

else:
    # Koodi tulostaa kaupunkia ei löydy tai avain ei toimi.
    print("Paikkakunta ei löydy tai avain ei toimi.")