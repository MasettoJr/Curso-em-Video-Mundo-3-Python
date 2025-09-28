from random import randint
from time import sleep
print('-' * 30)
print('JOGUE NA MEGA SENA')
print('-' * 30)

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []

for jogo in range(0, qtd_jogos):
    jogos.append(list())

print(f'SORTEANDO {qtd_jogos} JOGOS')
for i, jogo in enumerate(jogos):
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)

    jogo.sort()
    print(f'Jogo {i + 1}: {jogo}', end='\n')
    sleep(1)
