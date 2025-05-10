# Explicação
    Este é um app simples que realiza o desafio proposto.
    Ele acessa a API, realiza querys de teste e consultas de baterias agendadas ou passadas,
    como único usuário da base é john.doe@gmail.com, o app não pede input de usuário e as consultas
    de baterias são sempre filtradas para esse usuário.
    Ao ser executado o app perguntará se devem ser feitos os testes, caso seja respondido sim
    ele ira cumprir as etapas 1 a 3 do desafio e imprimir os resultados. 
    Na execução sem testes as etapas 4 e 5 são cumpridas.

# Como rodar o app
    Para executar o app é preciso um ambiente python3 com as bibliotecas pandas, numpy e requests
    instaladas. Basta executar o comando "pyhton3 src/app.py" no terminal.

## Imports
-requests para post
-json para tratar arquivos json

## Funções
- requisicao_post(username, password):
    Dado um username e um password, chama o metodo post como instruido no README
    e retorna o token ou o codigo de erro do post.

- consulta_DB(token, query)
    Dado um token e uma query, faz a consulta no banco e retorna um DataFrame pandas
    com os dados da consulta.

- PrintAgendamentosFuturo(token,emailUsuario):
    Dado um token e um email, retorna todos os agendamentos que ainda não aconteceram
    feitor pelo usuário dono daquele email.

- PrintAgendamentosPassado(token,emailUsuario):
    Dado um token e um email, retorna todos os agendamentos que já aconteceram
    feitor pelo usuário dono daquele email.

- TESTES():
    Realiza conexão com a API, executa 3 querys de teste e as imprime na tela. 


- Nome: Mateus Cursino Gomes Costa 
- CPF: 14889726640
- Email: mateuscgcosta@gmail.com
- Número: 31999964759
