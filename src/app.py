import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime

#Funções

def requisicao_post(username, password):

    url = "https://appsaccess.automy.com.br/login"  
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "username": username,
        "password": password
    }
    json_data = json.dumps(data)

    try:
        response = requests.post(url, headers=headers, data=json_data)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro na requisição: {response.status_code}")
            print(f"Mensagem de erro: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
        
def consulta_DB(token, query):
    url = "https://appsaccess.automy.com.br/api/api/desafio/custom/do/query" 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    data = {
        "query": query,
        "db": "desafio"
    }

    json_data = json.dumps(data)

    try:
        response = requests.post(url, headers=headers, data=json_data)

        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            return df
        else:
            print(f"Erro na requisição: {response.status_code}")
            print(f"Mensagem de erro: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    
def PrintAgendamentosFuturo(token,emailUsuario):
    HOJE  = datetime.now().strftime("%d/%m/%Y")
    query = f"SELECT * FROM desafio.cadastro_baterias_desafio WHERE email = '{emailUsuario}' AND STR_TO_DATE(data_agendamento,'%d/%m/%Y') >= STR_TO_DATE('{HOJE}','%d/%m/%Y') "
    dfconsulta = consulta_DB(token,query) 
    print(f"Ola {dfconsulta['nome'].iloc[0]},\nseus próximos agendamentos são:\n")
    for _,linha in dfconsulta.iterrows():
        print(f"Data: {linha['data_agendamento']}, Horário: {linha['horario_agendamento']}, para {linha['qtde_pessoas']} pessoas\n")
    print("Nos vemos em breve!")

def PrintAgendamentosPassados(token,emailUsuario):
    HOJE  = datetime.now().strftime("%d/%m/%Y")
    query = f"SELECT * FROM desafio.cadastro_baterias_desafio WHERE email = '{emailUsuario}' AND STR_TO_DATE(data_agendamento,'%d/%m/%Y') < STR_TO_DATE('{HOJE}','%d/%m/%Y') "
    dfconsulta = consulta_DB(token,query) 
    print(f"Ola {dfconsulta['nome'].iloc[0]},\nseus agendamentos passados são:\n")
    for _,linha in dfconsulta.iterrows():
        print(f"Data: {linha['data_agendamento']}, Horário: {linha['horario_agendamento']}, para {linha['qtde_pessoas']} pessoas\n")
    print("Nos vemos em breve!")


#Variaveis Globais
username = "fldoaogopdege"
senha = "ygalepsm"
emailUsuario = "john.doe@gmail.com"

def TESTES():
    #Teste token
    print('Teste token\n')
    retorno = requisicao_post(username=username, password=senha) 

    if retorno:
        token = retorno["token"]
        print(f"Token : {token}\n")
    else:
        print("Erro no post")

    #Teste query
    print('Teste query\n')
    query1 = "SELECT * FROM desafio.cadastro_baterias_desafio"
    print("query: ",query1)
    consultaTeste = consulta_DB(token=token,query=query1 )

    if consultaTeste is None:
        print("erro query")
        exit()
    print(consultaTeste)

    #Query MySQL personalizada
    print("Query MySQL personalizada")
    query2 = "SELECT * FROM desafio.cadastro_baterias_desafio WHERE horario_agendamento = '20h' "
    print("query: ",query2)

    consultaPersonalizada = consulta_DB(token=token,query=query2 )
    if consultaPersonalizada is None:
        print("erro query")
        exit()
    print(consultaPersonalizada)

    #Query para dados relacionados ao cliente
    print("Query para dados relacionados ao cliente")
    query3 = "SELECT * FROM desafio.cadastro_baterias_desafio WHERE email = 'john.doe@gmail.com'"
    print("query: ",query3)

    consulta = consulta_DB(token=token,query=query3 )
    if consulta is None:
        print("erro query")
        exit()
    print(consulta)


#Teste token
retorno = requisicao_post(username=username, password=senha) 

if retorno:
    token = retorno["token"]
else:
    print("Erro no post")

boolTeste = input("Rodar Testes?\n1-Sim\n2-Não\n")
if(not int(boolTeste)-1):
    TESTES()
    exit()
else:
    PrintAgendamentosFuturo(token,emailUsuario)
    boolPassadas = input("Deseja ver seus agendamentos passados?\n1-Sim\n2-Não\n")
    if(not int(boolPassadas)-1):
        PrintAgendamentosPassados(token,emailUsuario)


