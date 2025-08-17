def ler_lista(nome):
    q = int(input(f"Digite a quantidade de elementos da {nome}: "))
    print(f"Digite os {q} elementos da {nome}:")
    lst = []
    for i in range(q):
        lst.append(int(input()))
    return lst

lista1 = ler_lista("lista 1")
lista2 = ler_lista("lista 2")

intercalada = []
i = j = 0

while i < len(lista1) and j < len(lista2):
    intercalada.append(lista1[i])
    intercalada.append(lista2[j])
    i += 1
    j += 1

if i < len(lista1):
    intercalada.extend(lista1[i:])
if j < len(lista2):
    intercalada.extend(lista2[j:])

print("Lista intercalada:", *intercalada)