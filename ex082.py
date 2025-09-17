lista = []
lista_par = []
lista_impar = []
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    opcao = int(input('Continuar? 1 - Sim / 2 - Não '))
    if opcao == 2:
        break
    elif opcao != 1:
        print('Opção inválida!')

for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)



print(lista)
print(lista_par)
print(lista_impar)
