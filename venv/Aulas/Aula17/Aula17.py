# if / elif / else
# se / se não se / se não

entrada = input('Você quer entrar ou sair? ')

if entrada == "ENTRAR" or "entrar":
    print('Você entrou no sistema')

    print(12341234)
elif entrada == "SAIR" or "sair":
    print("Você saiu do sistema")

else:
    print("Você não digitou nem entrar e nem sair.")

print("Fora dos blocos.")