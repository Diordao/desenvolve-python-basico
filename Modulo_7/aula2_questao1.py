data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

partes = data.split("/")

dia = partes[0]
mes = int(partes[1])
ano = partes[2]

mes_extenso = meses[mes - 1]

print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")