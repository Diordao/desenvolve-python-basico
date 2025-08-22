frase = "Meu amor mora em Roma e me deu um ramo de flores"

count_vogais = 0
indices = []
for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        count_vogais += 1
        indices.append(i)
print(frase)
print(count_vogais)
print(indices)