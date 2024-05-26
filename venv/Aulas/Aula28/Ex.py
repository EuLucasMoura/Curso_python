nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if nome & idade == True:
    print('Seu nome é {}'.format(nome))
    print('Sua idade é {}'.format(idade))
    print('Seu nome de trás pra frente é:'.format(nome[-1]))