# Leitura de dados (entrada)
avaliacao = int(input("Qual a avaliação do filme (1 a 5): "))

# Processamento e impressão de dados (saída)
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular!")
elif avaliacao == 1:
    print("Ruim!")
else:
    print("Avaliação inválida. Digite um número de 1 a 5.")