import traceback
import sys
import requests

# Cabeçalho de acesso a API com o token.
headers = {
    "Accept": "application/json", 
    "authorization": "Bearer " + str(sys.argv[3]), # Captura o token enviado por argumento pelo robot framework
    "Accept": "application/json"
}

# Função responsável pela busca do id de uma região passado por parâmetro.
def getLocationId(region):
    try:
        response = requests.get("https://api.clashroyale.com/v1/locations", headers=headers)
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
            clanTag = clanTag.replace("#","%23") # Colocando o código do caractere "#"" na url baseado em ASCII Encoding Reference.

        url = "https://api.clashroyale.com/v1/clans/" + clanTag + "/members"

        response = requests.get(url, headers=headers)
        members = response.json()
        
        return members['items']
    except:
        print("[ERROR] Erro ao buscar os membros do clã com a tag " + clanTag)
        traceback.print_exc()

try:
    # Captura o primeiro e o segundo argumento na linha de comando.
    clanName = str(sys.argv[1]) 
    region = str(sys.argv[2])

    regionId = getLocationId(region)
    # Verifica se foi encontrado o id para a região informado.
    if regionId is None: 
        print("A região '" + region + "' não foi encontrada.")
        sys.exit()

    clanTag = getClanTag(clanName, regionId)
    # Verifica se foi o clã com o nome informado.
    if clanTag is None: 
        print("O clã '" + clanName + "' não foi encontrado.")
        sys.exit()

    members = getClanMembers(clanTag)

    # Imprime no console do sistema, o nome do clã mais a lista de todos os seus membros.
    print("\n\n[INÍCIO DO RELATÓRIO]\n")
    print("| Clã: " + clanName + " |")
    for member in members:
        print("| Nome: " + member['name'] + " | Level: " + str(member['expLevel']) + " | Troféus: " + str(member['trophies']) + " | Papel: " + member['role'] + " |")
    
    print("\n[FIM DO RELATÓRIO]\n\n")
    
except:
    # Verifica se o exception é derivado de um erro dos argumentos na linha de comando.
    if str(sys.exc_info()[0]) == "<class 'IndexError'>":        
        print("Por favor, refaça o comando no seguinte formato:\n\t python {arquivo.py} '{nome_do_clan}' '{regiao}' '{token}'")
        
    # Verifica se o exception é derivado da ordem de encerramento do script.
    elif str(sys.exc_info()[0]) != "<class 'SystemExit'>":      
        print("[ERROR] Erro na execução do script principal")
        traceback.print_exc()