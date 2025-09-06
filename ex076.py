listagem = (
    "Pão", 1.00,
    "Leite", 3.50,
    "Frango", 10.90,
    "Arroz", 5.20,
    "Ovos", 7.30,
    "Queijo", 12.50,
    "Manteiga", 8.40,
    "Macarrão", 4.60,
    "Feijão", 6.80,
    "Tomate", 3.90
)
mensagem = "LISTAGEM DE PREÇOS"
print(40 * "-")
print(f"{mensagem:^40}")
print(40 * "-")

for pos, item in enumerate(listagem):
    if pos % 2 == 0:
        print(f"{item:.<20}", end='')
        print(f"{'R$':.>15}", end='')

    if pos % 2 != 0:
        print(f"{listagem[pos]:>5}")
print(40 * "-")