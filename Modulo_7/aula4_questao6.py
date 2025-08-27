import csv

top_por_ano = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
        try:
            track_name = linha[0]
            artist_name = linha[1]
            artist_count = int(linha[2])
            released_year = int(linha[3])
            streams = int(linha[8])
        except (ValueError, IndexError):
            continue

        if 2012 <= released_year <= 2022:
            if released_year not in top_por_ano or streams > top_por_ano[released_year][3]:
                top_por_ano[released_year] = [track_name, artist_name, released_year, streams]

resultado = [top_por_ano[ano] for ano in sorted(top_por_ano.keys())]

print("=== Top músicas de 2012 a 2022 ===")
print(resultado)