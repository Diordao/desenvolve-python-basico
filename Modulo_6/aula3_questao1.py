# Entrada de dados e processamento
nums = []
print("Digite números inteiros (Enter em branco para encerrar). Mínimo de 4 valores.")
while True:
    s = input()
    if s.strip() == "":
        if len(nums) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números. Continue:")
            continue
    nums.append(int(s))

# Saídas
print("Lista original:", nums)

print("3 primeiros elementos:", nums[:3])
print("2 últimos elementos:", nums[-2:])

print("Lista invertida:", nums[::-1])

print("Elementos de índice par:", nums[0::2])
print("Elementos de índice ímpar:", nums[1::2])