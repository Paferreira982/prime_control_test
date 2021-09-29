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

*** Test Cases ***
Gerar Token
    Abrir Navegador

    Fazer Login

    Acessar Tela do Token

    Criar Nova Chave

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

