expressao = input('Digite uma expressão: ')
parenteses = []
for elemento in expressao:
    if '(' not in parenteses:
        parenteses.append('(')
    elif elemento == ')':
        parenteses.pop(0)
if parenteses == []:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
