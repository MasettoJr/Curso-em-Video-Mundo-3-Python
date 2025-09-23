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

for e in range(0, 9):
    print(f'[ {lista[e // 3][e % 3]} ] ', end='')
    if (e + 1) == 3 or (e + 1) == 6 or (e + 1) == 9:
        print('')
