lista = []
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    opcao = int(input('Continuar? 1 - Sim / 2 - Não ' ))
    if opcao == 2:
        break
    elif opcao != 1:
        print('Opção inválida!')

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')