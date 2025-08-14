# Leitura de dados (entrada)
n = int(input("Digite a quantidade de respondentes: "))

# Inicializar as variáveis
soma = 0 # resultado da soma
cont = 0 # variável de controle do loop

# Iterações
while cont < n:
    idade = int(input("Digite a idade: "))
    soma += idade #soma = soma + idade

    # atualizando a variável de controle do loop
    cont += 1 # cont = cont + 1

# Impressão de dados (saída)
print(f"A média das idades é {soma / n:,.2f} anos.")