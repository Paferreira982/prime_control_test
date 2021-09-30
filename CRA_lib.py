import os
from requests import get

# Acessa uma API pública para obter o endereço de IP externo da máquina.
def getPublicAdress():
    return get('https://api.ipify.org').text

# Função python para rodar o script principal com as config desejadas
def runPython(clanName, region, token):
    command = 'python main_script.py "' + clanName + '" ' + region + ' ' + token
    os.system(command)