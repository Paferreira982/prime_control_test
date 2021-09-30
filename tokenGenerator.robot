*** Settings ***
Library         Selenium2Library
Library         functions.py

*** Variables ***
${browser}      chrome
${URL}      https://developer.clashroyale.com/

${owner_name}      Pedro Augusto

${key_name}      Prime_control
${key_description}      Descricao simples

${email}      paferreira982@hotmail.com
${password}      senhaSimples

${clan_name}      The Resistance
${region}      Brazil
${token}      eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI3ODgxNzdmLWEwM2EtNDI5NS04ZWRjLWJjOTM3Mjg0NDVlYiIsImlhdCI6MTYzMjk1NzA1NSwic3ViIjoiZGV2ZWxvcGVyL2VmYTQ3NDFiLTA2MzUtMGNlNS0yNTA3LWFkYzhkZDk3YWQ4NiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMjUxLjIyNi4xMDYiXSwidHlwZSI6ImNsaWVudCJ9XX0.jy7XEhA2Aj5ae1BiuG7kUlHOAlcSKYzav-8ozERIVhT8pbAenO0EC7vPwF5OMzvafzvaNshx8faZYYWGpDDksQ

*** Test Cases ***
Gerar Token
    Abrir Navegador

#    Fazer Login

#    Acessar Tela do Token

#    Criar Nova Chave

    Fechar Navegador

*** Keywords ***
Abrir Navegador
    Open Browser        ${URL}      ${browser}

    Wait Until Element Is Visible       //div/a[text()="Log In"]

    Run Python        ${clan_name}      ${region}      ${token}


Fechar Navegador
    Close Browser


Fazer Login
    Click Element                   //div/a[text()="Log In"]

    Wait Until Element Is Visible       //button/span[text()="Log In"]

    Click And Input Text        //input[contains(@placeholder, "Email")]    ${email}

    Sleep            1 seconds

    Click And Input Text        //input[contains(@placeholder, "Password")]    ${password}

    Sleep            1 seconds

    Click Element                   //button/span[text()="Log In"]

    Wait Until Element Is Visible       //button/span[text()="${owner_name}"]


Acessar Tela do Token
    Click Element                   //button/span[text()="${owner_name}"]

    Sleep            1 seconds

    Click Element                   //div[contains(@class, "btn-group open")]/ul/li/a[text()="My Account"]

    Wait Until Element Is Visible       //a/span[text()="Create New Key"]


Criar Nova Chave
    Click Element                   //a/span[text()="Create New Key"]

    Wait Until Element Is Visible       //button/span[text()="Create Key"]

    Click And Input Text        //input[@id="name"]    ${key_name}

    Click And Input Text        //textarea[@id="description"]    ${key_description}

    ${ip_adress}        Get Public Adress

    Click And Input Text        //input[@id="range-0"]    ${ip_adress}

    Click Element                   //button/span[text()="Create Key"]

    Wait Until Element Is Visible            //h4[text()="${key_name}"]


Click And Input Text
    [Arguments]                     ${xpath}    ${value}
    
    Wait Until Element Is Visible   xpath=${xpath}
    Scroll Element Into View        xpath=${xpath}
    Click Element			        xpath=${xpath}
    Input Text   			        xpath=${xpath}  ${value}

