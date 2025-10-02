ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'nN':
        break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-' * 30)

while True:
    resposta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resposta == 999:
        break
    else:
        print(f'Notas de {ficha[resposta][0]} são {ficha[resposta][1][0]} e {ficha[resposta][1][1]}.')