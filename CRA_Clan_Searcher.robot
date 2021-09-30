*** Settings ***
Library         Selenium2Library
Library         CRA_lib.py

*** Variables ***
${browser}      chrome
${URL}      https://developer.clashroyale.com/

${owner_name}      Pedro Augusto

${key_name}      Prime_control

${email}      paferreira982@hotmail.com
${password}      senhaSimples

${clan_name}      The Resistance
${region}      Brazil

*** Test Cases ***
Gerar Token
    Abrir Navegador

    Fazer Login

    Acessar Tela do Token

    Verificar Token

    Rodar script principal

    Fechar Navegador

*** Keywords ***
Abrir Navegador
    Open Browser        ${URL}      ${browser}

    Wait Until Element Is Visible       //div/a[text()="Log In"]


Fechar Navegador
    Close Browser


Fazer Login
    Click Element                   //div/a[text()="Log In"]

    Wait Until Element Is Visible       //button/span[text()="Log In"]

    Clicar e Escrever        //input[contains(@placeholder, "Email")]    ${email}

    Sleep            1 seconds

    Clicar e Escrever        //input[contains(@placeholder, "Password")]    ${password}

    Sleep            1 seconds

    Click Element                   //button/span[text()="Log In"]

    Wait Until Element Is Visible       //button/span[text()="${owner_name}"]


Acessar Tela do Token
    Click Element                   //button/span[text()="${owner_name}"]

    Sleep            1 seconds

    Click Element                   //div[contains(@class, "btn-group open")]/ul/li/a[text()="My Account"]

    Wait Until Element Is Visible       //a/span[text()="Create New Key"]

Verificar Token
    ${ip_adress}        Get Public Adress

    ${status}=  Run Keyword And Return Status    Element Should Not Be Visible   //div/p[text()="${ip_adress}"]

    Run Keyword If    ${status}    Criar Nova Chave    ${ip_adress}


Criar Nova Chave
    [Arguments]                     ${ip_adress}

    Click Element                   //a/span[text()="Create New Key"]

    Wait Until Element Is Visible       //button/span[text()="Create Key"]

    Clicar e Escrever        //input[@id="name"]    ${key_name}

    Clicar e Escrever        //textarea[@id="description"]    ${ip_adress}

    Clicar e Escrever        //input[@id="range-0"]    ${ip_adress}

    Click Element                   //button/span[text()="Create Key"]

    Wait Until Element Is Visible            //h4[text()="${key_name}"]


Rodar script principal
    Click Element                   //h4[text()="${key_name}"]

    ${token}        Get Text        //samp

    Run Python        ${clan_name}      ${region}      ${token}


Clicar e Escrever
    [Arguments]                     ${xpath}    ${value}
    
    Wait Until Element Is Visible   xpath=${xpath}

    Click Element			        xpath=${xpath}

    Input Text   			        xpath=${xpath}  ${value}

