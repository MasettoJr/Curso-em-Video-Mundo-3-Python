numeros = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
)

while True:
    entrada = int(input("Digite um número entre 0 e 20: "))

    if 0 <= entrada <= 20:
        print(f"Você digitou o número {numeros[entrada]}.")
        opcao = int(input("Você quer continuar? 1 - SIM 2 - NÃO: "))
        while True:
            if opcao == 2:
                break
    else:
        print("Tente novamente.")
