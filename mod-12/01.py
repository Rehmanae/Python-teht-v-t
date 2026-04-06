import requests

# tämä on osoite, josta saadaan yksi vitsi
osoite = "https://api.chucknorris.io/jokes/random"

# lähetetään pyyntö nettiin
vastaus = requests.get(osoite)

# muutetaan vastaus python-sanakirjaksi
data = vastaus.json()

# otetaan vitsin teksti ja tulostetaan se
print(data["value"])
