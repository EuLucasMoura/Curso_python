"""
s - string
d - int 
f - float 
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
ex: 0>-100,.1f
conversion flags - !r !s !a
"""

variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:,.1f}')
print(f'O hexadecima de 1500 é {1500:08X}')