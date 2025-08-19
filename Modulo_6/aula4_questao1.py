# Todos os números pares entre 20 e 50 (inclusive)
pares_20_50 = [n for n in range(20, 51) if n % 2 == 0]
print("Os números pares entre 20 e 50 são:", pares_20_50)

# Quadrados dos valores da lista
orig = [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in orig]
print("Lista:", orig)
print("Os quadrados dos números da lista são:", quadrados)

# Todos os números entre 1 e 100 divisíveis por 7
div7 = [n for n in range(1, 101) if n % 7 == 0]
print("Todos os números entre 1 e 100 divisíveis por 7 são:", div7)

# 4) Par ou ímpar
par_ou_impar = ["par" if n % 2 == 0 else "impar" for n in range(0, 30, 3)]
print("Par/ímpar para range(0,30,3):", par_ou_impar)