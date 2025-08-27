import random

with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo.readlines()]
palavra_secreta = random.choice(palavras).lower()

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
estagios = conteudo.strip().split("=========\n")

tentativas = 6
erros = 0
letras_adivinhadas = []

progresso = ["_" for _ in palavra_secreta]

def imprime_enforcado(erros):
    print(estagios[erros])

print("=== Jogo da Forca ===")
print("Palavra:", " ".join(progresso))

while erros < tentativas and "_" in progresso:
    letra = input("Digite uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já tentou essa letra!")
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                progresso[i] = letra
        print("Acertou!")
    else:
        erros += 1
        print("Errou!")
        imprime_enforcado(erros)

    print("Palavra:", " ".join(progresso))

if "_" not in progresso:
    print("Parabéns, você venceu! A palavra era:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)