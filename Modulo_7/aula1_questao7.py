import random

def encrypt(lista):
    chave = random.randint(1, 10)
    
    criptografados = []

    for nome in lista:
        novo_nome = ""
        for c in nome:
            novo_codigo = ord(c) + chave

            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)

            novo_nome += chr(novo_codigo)
        criptografados.append(novo_nome)
    
    return criptografados, chave


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
resultado, chave = encrypt(nomes)
print("Nomes: ", nomes)
print("Chave usada:", chave)
print("Nomes criptografados:", resultado)