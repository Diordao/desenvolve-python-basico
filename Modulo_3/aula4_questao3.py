# Leitura de dados (entrada)
ano = int(input("Digite o ano: "))

# Processamento e impressão de dados (saída)
bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if bissexto:
    print("Ano bissexto!")
else:
    print("Ano não bissexto.")