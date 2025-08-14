# Leitura de dados (entrada)
n = int(input("Quantos números serão digitados? "))

# Inicializar as variáveis
maior = 0

# Iterações
while n > 0:

    x = int(input("Digite um número: "))
    if x > maior:
        maior = x
    n = n - 1    

# Impressão de dados (saída)
print("O maior número digitado foi:", maior)