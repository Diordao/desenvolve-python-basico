# Leitura de dados (entrada)
idade           = int(input("Digite sua idade: "))
quant_jogos     = input("Já jogou pelo menos 3 jogos de tabuleiro? (sim ou nao): ")
quant_vitorias  = int(input("Quantos jogos já venceu? "))

# Processamento
# A: o participante tiver entre 16 e 18 anos
# B: já tiver jogado pelo menos 3 jogos
# C: já ter vencido pelo menos 1 jogo
a = idade >= 16 and idade <= 18
b = quant_jogos == 'sim'
c = quant_vitorias >= 1

pode_ingressar = a and b and c

# Impressão de dados (saída)
print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_ingressar}")