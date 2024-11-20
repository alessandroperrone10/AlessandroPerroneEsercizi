# Create un programma python che permette tramite le api
# https://open-meteo.com/en/docs (per le previsioni metereologiche) e
# (per l’ottenimento in automatico della propria
# langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione
# metereologiche.
# L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
# visionare oltre che le temperature anche la velocità del vento e le
# probabili precipitazioni.


import json
import requests

risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.4643&longitude=9.1895&hourly=temperature_2m")

# print(risposta.json()['latitude'])

risposta_text = risposta.text

risposta_json = json.loads(risposta_text)
print(risposta_json['latitude'])