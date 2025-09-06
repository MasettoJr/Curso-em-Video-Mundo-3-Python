palavras = (
    "cachorro",
    "gato",
    "passaro",
    "computador",
    "celular",
    "livro",
    "caneta",
    "mesa",
    "cadeira",
    "janela",
    "porta",
    "carro"
)
vogais = ('a', 'e', 'i', 'o', 'u')
for palavras in palavras:
    print(f"Na palavra {palavras.upper()} temos ", end='')
    for letra in palavras:
        if letra in vogais:
            print(f"{letra} ", end='')
    print("")

