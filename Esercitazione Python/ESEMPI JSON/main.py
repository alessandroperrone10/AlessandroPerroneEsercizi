import json

fileJson = '{"chiave" : "valore", "chiave2" : "valore2"}'

print(type(fileJson))

fileJsonConvertito = json.loads(fileJson)

print(fileJsonConvertito)
