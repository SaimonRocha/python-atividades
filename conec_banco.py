# Importamos a biblioteca:
import pymysql
 
# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='python', user='root', passwd='')
 
# Cria um cursor:
cursor = conexao.cursor()
 
# Executa o comando:
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

cursor.execute("ALTER TABLE cadastro AUTO_INCREMENT = 1")
cursor.execute(f"INSERT INTO cadastro (email, senha) VALUES ('{email}', '{senha}')");

# Efetua um commit no banco de dados.
conexao.commit()
 
# Finaliza a conexão
conexao.close()