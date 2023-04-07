nome = 'Lucas Moura'
altura = float('1.75')
peso = float('70.0')
imc =  peso / (altura * altura)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa, {peso:.2f}KG.'
linha_3 = f'Seu imc é de, {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)