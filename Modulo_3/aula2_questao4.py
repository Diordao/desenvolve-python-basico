# Leitura de dados (entrada)
classe       = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Processamento
# A: Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
# B: Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
# C: Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.
a = classe == 'guerreiro' and pontos_forca >= 15 and pontos_magia <= 10
b = classe == 'mago' and pontos_forca <= 10 and pontos_magia >= 15
c = classe == 'arqueiro' and pontos_forca > 5 and pontos_forca <= 15 and pontos_magia > 5 and pontos_magia <= 15

pontos_consistentes = a or b or c

# Impressão de dados (saída)
print(f"Pontos de atributo consistentes com a classe escolhida: {pontos_consistentes}")