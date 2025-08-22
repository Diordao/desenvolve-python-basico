while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')

    if frase.lower() == "fim":
        break

    limpa = ""
    for char in frase:
        if char.isalpha():
            limpa += char.lower()

    if limpa == limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')