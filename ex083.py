expressao = input('Digite uma expressão: ')
lista = []

for letra in expressao:
    lista.append(letra)

if lista.count('(') == lista.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')



