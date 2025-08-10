# Leitura de dados
nome_produto1 = input("Digite o nome do produto 1: ")
preco_produto1 = float(input("Digite o preço unitário do produto 1: "))
quantidade_produto1 = int(input("Digite a quantidade do produto 1: "))

nome_produto2 = input("Digite o nome do produto 2: ")
preco_produto2 = float(input("Digite o preço unitário do produto 2: "))
quantidade_produto2 = int(input("Digite a quantidade do produto 2: "))

nome_produto3 = input("Digite o nome do produto 3: ")
preco_produto3 = float(input("Digite o preço unitário do produto 3: "))
quantidade_produto3 = int(input("Digite a quantidade do produto 3: "))

# Processamento

valor_total_produto1 = preco_produto1 * quantidade_produto1
valor_total_produto2 = preco_produto2 * quantidade_produto2
valor_total_produto3 = preco_produto3 * quantidade_produto3
valor_total_compra = valor_total_produto1 + valor_total_produto2 + valor_total_produto3

# Impressão de dados (saída)

print(f"O valor total do(a) {nome_produto1} é R$ {valor_total_produto1:,.2f}")
print(f"O valor total do(a) {nome_produto2} é R$ {valor_total_produto2:,.2f}")
print(f"O valor total do(a) {nome_produto3} é R$ {valor_total_produto3:,.2f}")
print(f"O valor total da compra é R$ {valor_total_compra:,.2f}")