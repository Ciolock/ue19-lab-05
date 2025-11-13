import requests

# API de blagues
url = "https://v2.jokeapi.dev/joke/Any"

response = requests.get(url)
data = response.json()

# Affichage de la blague
if data.get("type") == "single":
    print(data["joke"])
else:
    print(data["setup"])
    print(data["delivery"])
