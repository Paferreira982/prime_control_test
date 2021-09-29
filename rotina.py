import requests
import json
import traceback
from requests import get

publicIpAdress = get('https://api.ipify.org').text # Acessa uma API pública para obter o endereço de IP externo da máquina.

headers={
    "Accept": "application/json", 
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJlODA2ZjUzLWVmN2MtNGI3Yi1hNmZhLTRjZDMwZTA0MzJiOSIsImlhdCI6MTYzMjkzMDg1OSwic3ViIjoiZGV2ZWxvcGVyL2VmYTQ3NDFiLTA2MzUtMGNlNS0yNTA3LWFkYzhkZDk3YWQ4NiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMjUxLjIyNi4xMDYiXSwidHlwZSI6ImNsaWVudCJ9XX0.ydiaPSc-6R-Mw7GbxhyW0oLQI-3BfHwvVtpEJ2tgc9cM9jAQhwtfwW2VnY7Hrsh1t1Lw2fnZPLGpjHRPQnyKDQ",
    "Accept": "application/json"
} # Cabeçalho de acesso a API.

# Função responsável pela busca do id de um location passado por parâmetro.
def getLocationId(location):
    try:
        locations = requests.get("https://api.clashroyale.com/v1/locations", headers=headers)
        for loc in locations.json()['items']:
            if loc['name'] == location:
                return loc['id']
        return -1
    except:
        print("[ERROR] Erro ao buscar o id da localização: " + location)
        traceback.print_exc()

print(getLocationId("Brazil"))