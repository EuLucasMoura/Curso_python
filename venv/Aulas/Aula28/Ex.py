nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Sua idade é {idade}.')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A ultima letra do seu nome é {nome[-1]}.')

    if ' ' in nome:
        print("Seu nome contêm espaços")
    else:
        print("Seu nome não contêm espaços")
else:
    print("Desculpe, você deixou campos vazios")
    