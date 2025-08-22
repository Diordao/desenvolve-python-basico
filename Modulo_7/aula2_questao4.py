def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        else:
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha = input("Digite uma senha para validar: ")
if validador_senha(senha):
    print("Senha válida ✅")
else:
    print("Senha inválida ❌")