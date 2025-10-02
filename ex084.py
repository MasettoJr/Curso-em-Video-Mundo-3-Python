galera = []
pessoa_peso = []
menor = maior = 0
while True:
    pessoa_peso.append(str(input('Nome: ')))
    pessoa_peso.append(float(input('Peso: ')))
    galera.append(pessoa_peso[:])
    pessoa_peso.clear()
    continua = str(input('Quer continuar? [S/N] '))
    print(galera)
    if continua in 'nN':
        break

print(f'Ao todo. você cadastrou {len(galera)} pessoas.')

for i, pessoa in enumerate(galera):
    if i == 0:
        maior = menor = galera[i][1]
    if galera[i][1] > maior:
        maior = galera[i][1]
    elif galera[i][1] < menor:
        menor = galera[i][1]

print(f'O maior peso foi  de {maior:.1f}Kg. Peso de ', end='')
for i, pessoa in enumerate(galera):
    if galera[i][1] == maior:
        print(f'[{galera[i][0]}]', end=' ')
print(f'\nO menor peso foi  de {menor:.1f}Kg. Peso de ', end='')
for i, pessoa in enumerate(galera):
    if galera[i][1] == menor:
        print(f'[{galera[i][0]}]', end=' ')
