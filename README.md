<h2>Requisitos</h2>

<b>Python 3</b>
- https://www.python.org/downloads/ <br>

<b>Dependências</b>
- pip install requests


<b>Robot Framework</b>
- pip install robotframework
- pip install robotframework-selenium2library


<h2>Para executar</h2>

<b>Para executar a aplicação</b>
- robot CRA_Clan_Searcher.robot

<h2>Decisões tomadas</h2>
  
<b>Aplicação e regra de negócio</b>
- Optei por realizar todas as tarefas através de um único comando (no Robot Framework). O script fará toda a lógica de verificação de "keys" na API, caso haja uma key existente para o IP da máquina onde o script está rodando ele não criará outra key. Assim toda a informação ficará disponível em um único console.
- Utilizei uma API pública (ipify) para obter o IP público da máquina de forma dinâmica.
- Para simplificar os comandos para o usuário, decidi que o próprio Robot Framework construirá os argumentos em conjunto com uma "mini-lib" python, feita por mim, busca o IP e envia um comando diretamente no sistema para executar o script principal, que busca as informações solicitadas e informadas dentro do próprio script através de variáveis.


<b>Observações</b>
- O "CRA" no nome dos arquivos é uma abreviação de "Clash Royale API"
- Arquivos com ".html", ".xml" e ".png" foram adicionados ao git ignore, afim de não poluir o repositório com os logs do Robot Framework
