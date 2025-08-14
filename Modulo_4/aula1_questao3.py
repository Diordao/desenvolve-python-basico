# Leitura de dados (entrada)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Processamento e impressão de dados (saída)
m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado!")
elif m >= 40 and m < 60:
    print("Recuperação!")
else:
    print("Reprovado!")

print("Fim!")