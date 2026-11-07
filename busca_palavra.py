import re

texto = input("Digite o título do livro: ")
letra = input("Digite a letra inicial para pesquisa: ")

resultado = re.findall(rf"\b{letra}[a-zà-ÿ]*", texto, re.IGNORECASE)

print()
print(resultado)

# Encontrando palavras que começam com uma letra específica
# Discutir no fórum

# Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema. Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra, para criar coleções temáticas baseadas em letras específicas. Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra, ajudando na organização ou em campanhas como “Livros com A para você!”.

# Como você criaria um programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?

# Exemplo de Entrada:

# Digite o título do livro: As Aventuras de Alice no País das Maravilhas
# Digite a letra inicial para pesquisa: A

# Saída esperada:

# ["As", "Aventuras", "Alice"]
