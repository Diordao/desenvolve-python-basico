# Lista de vogais em português
vogais = [
    'a','e','i','o','u',
    'A','E','I','O','U',
    'á','é','í','ó','ú',
    'Á','É','Í','Ó','Ú',
    'â','ê','ô','Â','Ê','Ô',
    'ã','õ','Ã','Õ'
]

# Mapa para normalizar vogais na ordenação
normaliza = {
    'á':'a','Á':'A','â':'a','Â':'A','ã':'a','Ã':'A',
    'é':'e','É':'E','ê':'e','Ê':'E',
    'í':'i','Í':'I',
    'ó':'o','Ó':'O','ô':'o','Ô':'O','õ':'o','Õ':'O',
    'ú':'u','Ú':'U'
}

# Solicitar frase
frase = input("Digite uma frase: ")

# Lista de vogais
lista_vogais = [ch for ch in frase if ch in vogais]

# Lista de consoantes
lista_consoantes = [ch for ch in frase if (ch not in vogais and ch != " " and ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'))]

# Ordenar vogais considerando equivalência acentuada
lista_vogais.sort(key=lambda x: normaliza.get(x, x).lower() if 'A' <= x <= 'Z' or 'a' <= x <= 'z' else normaliza.get(x, x))

# Exibir
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)