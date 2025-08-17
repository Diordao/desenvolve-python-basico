import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for i in range(num_elementos)]

soma = sum(elementos)
media = soma / len(elementos)

print(f"Quantidade sorteada: {num_elementos}")
print(f"Lista elementos: {elementos}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")