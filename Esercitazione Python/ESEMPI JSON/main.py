import json


def cobnversione_diz():
    fileJson = '{"chiave" : "valore", "chiave2" : "valore2"}'
    fileJsonConvertito = json.loads(fileJson)

    print(fileJsonConvertito)


dizionario = {"chiave" : "valore", "chiave2" : "valore2"}

fileJson = json.dumps(dizionario)

print(fileJson)