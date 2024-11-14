import json
import requests

risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.4643&longitude=9.1895&hourly=temperature_2m")

# print(risposta.json()['latitude'])

risposta_text = risposta.text

risposta_json = json.loads(risposta_text)
print(risposta_json['latitude'])