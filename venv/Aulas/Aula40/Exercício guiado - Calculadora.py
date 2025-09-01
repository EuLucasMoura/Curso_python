""" Minha solução
opcao = 0
resultado = 0
while opcao != "5":
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    print("="* 10 + " Calculadora " + "=" * 10)
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Dividir")
    print("[4] Multiplicar")
    print("[5] Sair\n")
    print("=" * 33)
    opcao = int(input("Escolha a operação: "))
    if opcao == 1:
        resultado = n1 + n2
        print(f"A soma de {n1} e {n2} é igual a {resultado}")
    elif opcao == 2:
        resultado = n1 - n2
        print(f"A subrtração de {n1} e {n2} é igual a {resultado}")
    elif opcao == 3:
        resultado = n1 / n2
        print(f"A divisão entre {n1} e {n2} é igual a {resultado}")
    elif opcao == 4:
        resultado = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é igual a {resultado}")
    elif opcao == 5:
        print("Saindo do programa...")
        break
print("Calculadora encerrada.")
"""

linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1
 