# Leitura de dados (entrada)
distancia = int(input("Digite a distância (km): "))
peso = float(input("Digite o peso (kg): "))

# Processamento e impressão de dados (saída)
if distancia <= 100 and peso <= 10:
    valor_frete = peso * 1
    print(f"O valor do frete é R$ {valor_frete:,.2f}")
elif distancia <= 100 and peso > 10:
    valor_frete = (peso * 1) + 10
    print(f"O valor do frete é R$ {valor_frete:,.2f}")
elif distancia >= 101 and distancia <= 300 and peso <= 10:
    valor_frete = peso * 1.50
    print(f"O valor do frete é R$ {valor_frete:,.2f}")
elif distancia >= 101 and distancia <= 300 and peso > 10:
    valor_frete = (peso * 1.50) + 10
    print(f"O valor do frete é R$ {valor_frete:,.2f}")
elif distancia >= 301 and peso <= 10:
    valor_frete = peso * 2
    print(f"O valor do frete é R$ {valor_frete:,.2f}")
elif distancia >= 301 and peso > 10:
    valor_frete = (peso * 2) + 10
    print(f"O valor do frete é R$ {valor_frete:,.2f}")