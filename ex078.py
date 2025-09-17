lista = []
for v in range(0, 5):
    valor = int(input(f"Digite um valor para a posição {v}: "))
    lista.append(valor)
maior_valor = max(lista)
menor_valor = min(lista)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} nas posições", end=" ")
for index, v in enumerate(lista):
    if v == maior_valor:
        print(f"{index}...", end=" ")
print(f"\nO menor valor digitado foi {min(lista)} nas posições", end=" ")
for index, v in enumerate(lista):
    if v == menor_valor:
        print(f"{index}...", end=" ")
