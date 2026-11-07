import re

texto = input("Digite o nome completo e o ano de nascimento do paciente: ")


nome_completo = re.findall(r"[a-zà-ÿ]+", texto, re.IGNORECASE)
nascimento = re.search(r"\b\d{4}\b", texto)

if not nome_completo and not nascimento:
    print("Formato invalido")
elif not nome_completo:
    print("Formato invalido: Insira o nome.")
elif not nascimento:
    print("Formato invalido: Informe a data no formato aaaa")
else:
    nome: str = nome_completo.pop(0).title()
    sobrenome = " ".join(nome_completo).title()

    print(f"Primeiro Nome: {nome}")
    if sobrenome == "":
        print("Sobrenome: Não Informado")
    else:
        print(f"Sobrenome: {sobrenome}")

    print(f"Ano de Nascimento: {nascimento.group()}")


# Agrupando informações dos pacientes

# Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados. Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". Por exemplo, “Monalisa Silva - 1994”.

# Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.

# Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.

# Exemplo de Entrada:

# Digite o nome completo e o ano de nascimento do paciente: Ana Silva - 1990

# Saída esperada:

# Primeiro Nome: Ana
# Sobrenome: Silva
# Ano de Nascimento: 1990
