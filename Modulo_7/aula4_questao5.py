livros = [
    ("O Caçador de Pipas", "Khaled Hosseini", 2003, 368),
    ("Torto Arado", "Itamar Vieira Junior", 2019, 264),
    ("Dom Casmurro", "Machado de Assis", 1899, 256),
    ("1984", "George Orwell", 1949, 328),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("Grande Sertão: Veredas", "Guimarães Rosa", 1956, 608),
    ("A Revolução dos Bichos", "George Orwell", 1945, 152),
    ("A Metamorfose", "Franz Kafka", 1915, 104),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 224),
]

with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    for titulo, autor, ano, paginas in livros:
        arquivo.write(f"{titulo},{autor},{ano},{paginas}\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")