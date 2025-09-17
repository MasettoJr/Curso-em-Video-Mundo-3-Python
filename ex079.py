lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    opcao = str(input("Quer continuar? [S/N]: ")).strip()
    if opcao in "Nn":
        break
print(f"Você digitou os valores {sorted(lista)}")
