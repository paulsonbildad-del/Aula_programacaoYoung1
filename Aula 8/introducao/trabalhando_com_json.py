import json

config = {

    "nome": "Sistema Escolar",
    "tema": "escuro",
    "volume": 75,
    "atualizado": True
}

with open("config.json", "w", encoding= "utf-8") as arquivo:
    json.dump(config,arquivo,indent=4)


with open("config.json", "r", encoding= "utf-8") as arquivo:
    config = json.load(arquivo)

print("config", config)
print("config", config["tema"])
print("config", config["volume"])



