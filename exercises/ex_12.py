import json

arquivo = open('person.json')
dados_json = json.load(arquivo)
print(dados_json)
