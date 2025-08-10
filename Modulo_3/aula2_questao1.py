# Leitura de dados (entrada)
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Processamento
# True se ambos forem maior de idade
# <exp1> juliana é maior de idade
# <exp2> cris é maior de idade
# <exp1> and <exp2>
# False em qualquer outro caso
pode_entrar = idade_juliana > 17 and idade_cris > 17

# Impressão de dados (saída)
print(f"Podem entrar no bar: {pode_entrar}")