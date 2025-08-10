# Leitura de dados (entrada)
genero = input("Digite o gênero (feminino ou masculino): ")
idade  = int(input("Digite a idade: "))
tempo  = int(input("Digite o tempo de serviço: "))

# Processamento
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos.
# C: Ou ter 60 anos  e trabalhado pelo menos 25.
a = (genero == 'feminino' and idade >= 60) or (genero == 'masculino' and idade >= 65)
b = tempo >= 30
c = idade >= 60 and tempo >= 25

pode_aposentar = a or b or c

# Impressão de dados (saída)
print(f"Pode aposentar: {pode_aposentar}")