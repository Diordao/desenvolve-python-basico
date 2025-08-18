import random

# Entrada
nums = [random.randint(-10, 10) for i in range(20)]
print("Original:", nums)

# Processamento
inicio_fatia_maior = 0
tam_fatia_maior = 0

inicio_fatia_atual = 0
tam_fatia_atual = 0

for i in range(len(nums)):
    if nums[i] < 0:        
        tam_fatia_atual += 1
        if tam_fatia_atual == 1:            
            inicio_fatia_atual = i
    else:        
        if tam_fatia_atual > tam_fatia_maior:
            tam_fatia_maior = tam_fatia_atual
            inicio_fatia_maior = inicio_fatia_atual
        tam_fatia_atual = 0

if tam_fatia_atual > tam_fatia_maior:
    tam_fatia_maior = tam_fatia_atual
    inicio_fatia_maior = inicio_fatia_atual

if tam_fatia_maior > 0:
    del nums[inicio_fatia_maior : inicio_fatia_maior + tam_fatia_maior]

# Saída
print("Editada:", nums)