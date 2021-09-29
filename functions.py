from requests import get

# Acessa uma API pública para obter o endereço de IP externo da máquina.
def getPublicAdress():
    return get('https://api.ipify.org').text