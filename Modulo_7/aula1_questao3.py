frase = "Meu amor mora em Roma e me deu um ramo de flores"

count_espacos = 0
indices = []
for i in range(len(frase)):
    if frase[i] in " ":
        count_espacos += 1
        indices.append(i)
print(frase)
print(count_espacos)
print(indices)