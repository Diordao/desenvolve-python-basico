# Leitura de dados (entrada)
n = int(input("Digite a quantidade de experimentos: "))

# Inicializar as variáveis
cont = 0 # variável de controle do loop
soma_coelho, soma_rato, soma_sapo = 0, 0, 0

# Iterações
while cont < n:
    quantia = int(input("Digite a quantidade de cobaias: "))
    tipo = input("c(coelho), r(rato) ou s(sapo): ")

    if tipo == 'c':
        soma_coelho += quantia
    elif tipo == 'r':
        soma_rato += quantia
    elif tipo == 's':
        soma_sapo += quantia
    else:
        print(f"Tipo {tipo} não reconhecido!")

    cont += 1

# Impressão de dados (saída)
print("Total de cobaias:", soma_coelho + soma_rato + soma_sapo)
print("Total de coelhos:", soma_coelho)
print("Total de ratos:", soma_rato)
print("Total de sapos:", soma_sapo)
print(f"Percentual de coelhos: {((soma_coelho / (soma_coelho + soma_rato + soma_sapo)) * 100):,.2f} %")
print(f"Percentual de ratos: {((soma_rato / (soma_coelho + soma_rato + soma_sapo)) * 100):,.2f} %")
print(f"Percentual de sapos: {((soma_sapo / (soma_coelho + soma_rato + soma_sapo)) * 100):,.2f} %")