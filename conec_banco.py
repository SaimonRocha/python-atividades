# Esse programa ao ser executado ele irá salvar no seu banco de dados
# As cidades para que o projeto funcione
# Para isso tenha o Pyhton no seu PC e execute o py nome_projeto
# Não esqueça de ter o banco de dados conectado

# Importamos a biblioteca:
import json     #Abertura de Json

#Função para remover os caracteres indesejados
def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

# Abrimos uma conexão com o banco de dados:
conexao = psycopg2.connect(host="localhost", database="crud", user="postgres", password="123")

# Cria um cursor:
cursor = conexao.cursor()

if(conexao):
    print('Conectado com Sucesso!')
else:
    print('Erro ao abrir conexão')


# Efetua um commit no banco de dados.
conexao.commit()

# Finaliza a conexão
conexao.close()
