texto = input("Digite o nome do produto: ")
texto_tratado = " ".join(texto.split()).title()

print(f"Produto informado: {texto_tratado}")


# Ajustando nomes de produtos
# Discutir no fórum

# Victor trabalha em um sistema de e-commerce e precisa organizar os nomes dos produtos que estão sendo cadastrados pelos lojistas. Esses nomes geralmente vêm com letras misturadas entre maiúsculas e minúsculas, além de espaços desnecessários no início e no final.

# Ajude Victor a criar um programa que receba um nome de produto e o padronize, deixando todas as letras minúsculas e removendo os espaços extras.

# Exemplo de Entrada:

# Digite o nome do produto: ChocoLAte Branco

# Saída esperada:

# chocolate branco
