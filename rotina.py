import traceback
import sys
import requests
from requests import get

# Acessa uma API pública para obter o endereço de IP externo da máquina.
publicIpAdress = get('https://api.ipify.org').text

# Cabeçalho de acesso a API com o token.
headers = {
    "Accept": "application/json", 
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJlODA2ZjUzLWVmN2MtNGI3Yi1hNmZhLTRjZDMwZTA0MzJiOSIsImlhdCI6MTYzMjkzMDg1OSwic3ViIjoiZGV2ZWxvcGVyL2VmYTQ3NDFiLTA2MzUtMGNlNS0yNTA3LWFkYzhkZDk3YWQ4NiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMjUxLjIyNi4xMDYiXSwidHlwZSI6ImNsaWVudCJ9XX0.ydiaPSc-6R-Mw7GbxhyW0oLQI-3BfHwvVtpEJ2tgc9cM9jAQhwtfwW2VnY7Hrsh1t1Lw2fnZPLGpjHRPQnyKDQ",
    "Accept": "application/json"
}

# Função responsável pela busca do id de uma região passado por parâmetro.
def getLocationId(region):
    try:
        response = requests.get("https://api.clashroyale.com/v1/locations", headers=headers).json()
        locations = response.json()

        for loc in locations['items']: # Verifica o json vindo da API, item por item, afim de econtrar o id da região solicitada.
            if loc['name'] == region:
                return loc['id']
        return
    except:
        print("[ERROR] Erro ao buscar o id da região: " + region)
        traceback.print_exc()

# Função responsável por capturar a tag de um clan, pelo nome e pelo regionId.
def getClanTag(clanName, regionId):
    try:
        params = {
            "name": clanName,
            "locationId": regionId,
            "limit": 1
        }

        reponse = requests.get("https://api.clashroyale.com/v1/clans", headers=headers, params=params)
        clan = reponse.json()

        if len(clan['items']) == 0: # Verifica se o comprimento da lista vinda da API é igual à zero, caracterizando que o valor buscado não foi encontrado.
            return

        return clan['items'][0]['tag']
    except:
        print("[ERROR] Erro ao buscar a tag do clã " + clanName)
        traceback.print_exc()

# Função responsável por buscar todos os membros de um clã pela tag.
def getClanMembers(clanTag):
    try:
        if "#" in clanTag:
            clanTag = clanTag.replace("#","%23") # Colocando o código do caractere # na url baseado em: ASCII Encoding Reference.

        url = "https://api.clashroyale.com/v1/clans/" + clanTag + "/members"

        response = requests.get(url, headers=headers)
        members = response.json()
        
        return members['items']
    except:
        print("[ERROR] Erro ao buscar os membros do clã com a tag " + clanTag)
        traceback.print_exc()

try:
    clanName = str(sys.argv[1]) # Captura o primeiro argumento na linha de comando.
    region = str(sys.argv[2]) # Captura o segundo argumento na linha de comando.

    regionId = getLocationId(region)
    if regionId is None: # Verifica se foi encontrado o id para a região informado.
        print("A região '" + region + "' não foi encontrada.")
        sys.exit()

    clanTag = getClanTag(clanName, regionId)
    if clanTag is None: # Verifica se foi o clã com o nome informado.
        print("O clã '" + clanName + "' não foi encontrado.")
        sys.exit()

    members = getClanMembers(clanTag)
    print("| Clã: " + clanName + " |")
    for member in members:
        print("| Nome: " + member['name'] + " | Level: " + str(member['expLevel']) + " | Troféus: " + str(member['trophies']) + " | Papel: " + member['role'] + " |")
    
except:
    if str(sys.exc_info()[0]) == "<class 'IndexError'>": # Verifica se o exception é derivado de um erro dos argumentos na linha de comando.
        print("Por favor, refaça o comando no seguinte formato:\n\t python3 {arquivo.py} '{nome_do_clan}' '{regiao}'")
    elif str(sys.exc_info()[0]) != "<class 'SystemExit'>": # Verifica se o exception é derivado da ordem de fechamento do programa.
        print("[ERROR]")
        traceback.print_exc()