frase = input("Digite uma frase: ")

vogais = "aáàâãäAÁÀÂÃÄeéêëEÉÊËiíîïIÍÎÏoóòôõöOÓÒÔÕÖuúùûüUÚÙÛÜ"

nova_frase = ""
for char in frase:
    if char in vogais:
        nova_frase += "*"
    else:
        nova_frase += char

print("Frase modificada:", nova_frase)