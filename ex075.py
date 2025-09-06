numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite mais um número: "))
numero4 = int(input("Digite o último número: "))
tupla = (numero1, numero2, numero3, numero4)
tupla_par = (
    numero1 if numero1 % 2 == 0 else "",
    numero2 if numero2 % 2 == 0 else "",
    numero3 if numero3 % 2 == 0 else "",
    numero4 if numero4 % 2 == 0 else ""
)

print(f"\nVocê digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
print(
    f"O valor 3 apareceu na {tupla.index(3) + 1}ª posição" if 3 in tupla else "O valor 3 não foi digitado em nenhuma posição"
)
print(f"Os valores pares digitados foram ", end='')
for numero in tupla_par:
    if numero != "":
        print(f"{numero} ", end='')





