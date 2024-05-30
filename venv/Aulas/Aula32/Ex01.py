""" Exercício 1
numero = int(input("Digite um número inteiro: "))
if type(numero) == int:
    if numero % 2 != 0:
        print(f"O número {numero} é ímpar.")
    else:
        print(f"O número {numero} é par.")
else:
    print("O número digitado não é um inteiro.")
"""

""" Exercicio 2
hora = int(input("Que horas são?(0-23) "))

if hora < 11:
    print("Bom dia!")
elif 12 <= hora <= 17:
    print("Boa tarde!")
elif 18 <= hora <=23:
    print("Boa noite!")
else:
    print("Hora inválida!")
"""

nome = input("Digite seu primeiro nome: ")

quantidade_caracteres = len(nome)

if quantidade_caracteres <= 4:
    print("Seu nome é curto.")
elif  5 == quantidade_caracteres <= 6:
    print("Seu nome é normal.")
elif quantidade_caracteres > 6:
    print("Seu nome é grande.")