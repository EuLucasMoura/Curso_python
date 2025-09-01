import os
produtos = []

def menu():
    print("-" * 5 + ' Menu de Produtos ' + "-" * 5)
    print("-" * 5 + ' Digite 1 para adicionar ' + "-" * 5)
    print("-" * 5 + ' Digite 2 para remover ' + "-" * 5)
    print("-" * 5 + ' Digite 3 para listar ' + "-" * 5)
    print("-" * 5 + ' Digite 4 para sair ' + "-" * 5)

while True:  # mais legível que while 1 != 0
    menu()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        produto = input('Insira um produto: ')
        produtos.append(produto)
    elif opcao == 4:  # condição de saída
        break

print('Programa encerrado.')
