lista = []

for indice in range(5):
    numero = int(input("Digite um valor: "))
    if lista == []:
        lista.append(numero)
        print(f"{numero} adicionado na lista vazia.")

    else:
        pos = 0
        while pos < len(lista):
            if numero < lista[pos]:
                lista.insert(pos, numero)
                print(f"{numero} adicionado na posição {pos} da lista.")
                break
            pos += 1

        else:
            lista.append(numero)
            print(f"{numero} adicionado no final da lista.")
print(lista)



