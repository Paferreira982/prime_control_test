import os
from requests import get

# Acessa uma API pública para obter o endereço de IP externo da máquina.
def getPublicAdress():
    return get('https://api.ipify.org').text

# Função python para alterar o token no python principal
def runPython(clanName, region, token):
    command = 'python rotina.py "' + clanName + '" ' + region + ' ' + token
    os.system(command)