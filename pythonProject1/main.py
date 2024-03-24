# Importa o Regex
import re

# Pede ao usuário um número de CPF
cpf = input("Digite um número de CPF: ")
cpf_validator = r'\b[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}\b'

# Pesquisa e compara a validação
if re.search(cpf_validator, cpf):
    print(f"O seu CPF é {cpf}")
else:
    print("Digite um CPF válido!")
