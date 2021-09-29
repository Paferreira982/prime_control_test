import traceback
import requests
from requests import get

# Acessa uma API pública para obter o endereço de IP externo da máquina.
publicIpAdress = get('https://api.ipify.org').text

# Cabeçalho de acesso a API.
headers = {
    "Accept": "application/json", 
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJlODA2ZjUzLWVmN2MtNGI3Yi1hNmZhLTRjZDMwZTA0MzJiOSIsImlhdCI6MTYzMjkzMDg1OSwic3ViIjoiZGV2ZWxvcGVyL2VmYTQ3NDFiLTA2MzUtMGNlNS0yNTA3LWFkYzhkZDk3YWQ4NiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMjUxLjIyNi4xMDYiXSwidHlwZSI6ImNsaWVudCJ9XX0.ydiaPSc-6R-Mw7GbxhyW0oLQI-3BfHwvVtpEJ2tgc9cM9jAQhwtfwW2VnY7Hrsh1t1Lw2fnZPLGpjHRPQnyKDQ",
    "Accept": "application/json"
}

# Função responsável pela busca do id de uma região passado por parâmetro.
def getLocationId(region):
    try:
        locations = requests.get("https://api.clashroyale.com/v1/locations", headers=headers)

        for loc in locations.json()['items']:
            if loc['name'] == region:
                return loc['id']
        return -1
    except:
        print("[ERROR] Erro ao buscar o id da região: " + region)
        traceback.print_exc()

#Função responsável por capturar a tag de um clan, pelo nome e pelo regionId
def getClanTag(clanName, regionId):
    try:
        params = {
            "name": clanName,
            "locationId": regionId,
            "limit": 1
        }
        clan =  requests.get("https://api.clashroyale.com/v1/clans", headers=headers, params=params)
        return clan.json()['items'][0]['tag']
    except:
        print("[ERROR]")
        traceback.print_exc()

def getClanMembers(clanTag):
    try:
        if "#" in clanTag:
            clanTag = clanTag.replace("#","%23") #Colocando o código do caractere # na url baseado em: ASCII Encoding Reference

        print(clanTag)
        url = "https://api.clashroyale.com/v1/clans/"+clanTag+"/members"
        members = requests.get(url, headers=headers)
        return members.json()['items']
    except:
        print("[ERROR]")
        traceback.print_exc()

print(getClanMembers(getClanTag("The Resistance", getLocationId("Brazil"))))