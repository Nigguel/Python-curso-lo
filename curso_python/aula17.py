# Operadores lógicos: and / or / not
# and: todas as condiçoes precisam ser verdadeiras.
# or: Qualquer condiçao verdadeira avalia toda a expressao como verdadeira.
# Sao considerados falsy: 0 0.0 '' False
# None: é usado pára representar um nao valor

# AND / OR
entrada = input("entrar [E] / sair [S]: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")
