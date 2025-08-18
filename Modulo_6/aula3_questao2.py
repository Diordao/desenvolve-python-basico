#Entrada
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

#Processamento
# 'www.' e '.com' têm 4 caracteres -> fatiar de [4 : -4]
dominios = [u[4:-4] for u in urls]

# Saídas
print("URLs:", urls)
print("dominios:", dominios)