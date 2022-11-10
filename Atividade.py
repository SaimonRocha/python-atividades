# Faça um Programa que peça dois números e imprima o maior deles.
def verificaMaiorNumero(a, b):
    if a > b:
        print(f"O maior número é {a}")
    else:
        print(f"O maior número é {b}")

# verificaMaiorNumero(12, 24)

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def verificaNegativoPositivo():
    if a < 0:
        print(f"O número {a} é negativo")
    else:
        print(f"O número {a} é positivo")
#verificaNegativoPositivo(-12)

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def verificaLetra(a):
    a = a.upper()
    if a == "M":
        print("O sexo digitado foi Masculino")
    elif a == "F":
        print("O sexo digitado foi Feminino")
    else:
        print("O sexo digitado é invalido")

# verificaLetra("f")

