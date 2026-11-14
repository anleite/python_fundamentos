
# Solicitando o CPF ao usuário
cpf = input("Digite seu CPF: ")

# Realizando a remoção do . e - e armazenando o CPF limpo
cpf_limpo = cpf.replace(".", "").replace("-", "")

# Apresentando o resultado do CPF limpo
print(f"CPF Limpo: {cpf_limpo}")
