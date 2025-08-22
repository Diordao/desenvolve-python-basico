cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

cpf_numeros = cpf.replace(".", "").replace("-", "")
nove_digitos = cpf_numeros[:9]

soma = 0
multiplicador = 10
for digito in nove_digitos:
    soma += int(digito) * multiplicador
    multiplicador -= 1

resto = soma % 11
if resto < 2:
    primeiro_digito = 0
else:
    primeiro_digito = 11 - resto

dez_digitos = nove_digitos + str(primeiro_digito)

soma = 0
multiplicador = 11
for digito in dez_digitos:
    soma += int(digito) * multiplicador
    multiplicador -= 1

resto = soma % 11
if resto < 2:
    segundo_digito = 0
else:
    segundo_digito = 11 - resto

cpf_calculado = nove_digitos + str(primeiro_digito) + str(segundo_digito)

if cpf_calculado == cpf_numeros:
    print("Válido")
else:
    print("Inválido")