a = []
b = []
c = []
lista = [a, b, c]

for v in range(0, 9):
    if v // 3 == 0:
        a.append(int(input(f'Digite um valor para a [{v // 3}, {v % 3}]: ')))
    elif v // 3 == 1:
        b.append(int(input(f'Digite um valor para a [{v // 3}, {v % 3}]: ')))
    else:
        c.append(int(input(f'Digite um valor para a [{v // 3}, {v % 3}]: ')))

print('-=-' * 10)
for e in range(0, 9):
    print(f'[ {lista[e // 3][e % 3]} ] ', end='')
    if (e + 1) == 3 or (e + 1) == 6 or (e + 1) == 9:
        print('')
print('-=-' * 10)

soma = 0
for elemento in lista:
    for elemento2 in elemento:
        if elemento2 % 2 == 0:
            soma += elemento2
print(f'A soma dos valores pares é {soma}.')

soma3col = 0
for elemento in lista:
    for i, elemento2 in enumerate(elemento):
        if i == 2:
            soma3col += elemento2
print(f'A soma dos valores da terceira coluna é {soma3col}.')

maior_valor = 0
for i, elemento in enumerate(lista):
    if i == 1:
        maior_valor = max(elemento)
print(f'O maior valor da segunda linha é {maior_valor}.')