par = []
impar = []
valor = [par, impar]

for v in range(0, 7):
    numero = int(input('Digite um valor: '))

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f"Os valores pares digitados foram: {sorted(par)}")
print(f"Os valores ímpares digitados foram: {sorted(impar)}")
