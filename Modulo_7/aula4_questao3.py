with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print("=== Primeiras 25 linhas ===")
for i in range(25):
    print(linhas[i], end="")

print("\n=== Número total de linhas ===")
print(len(linhas))

linha_maior = max(linhas, key=len)
print("\n=== Linha com mais caracteres ===")
print(linha_maior)

texto_completo = "".join(linhas).lower()

cont_nonato = sum(1 for palavra in texto_completo.split() if "nonato" == palavra.strip(".,;:!?()"))
cont_iria   = sum(1 for palavra in texto_completo.split() if "íria" == palavra.strip(".,;:!?()"))

print("\n=== Contagem de personagens ===")
print(f"Nonato: {cont_nonato}")
print(f"Íria: {cont_iria}")