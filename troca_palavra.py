texto = input("Digite o texto a ser revisado: ")
revisar = input("Qual palavra deseja substituir? ")
substitua = input("Qual a nova palavra? ")

novo_texto = texto.replace(revisar, substitua)

print(novo_texto)

# Substituindo palavras específicas

# Natalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". Para economizar tempo, Natalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.

# Ajude Natalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as alterações aplicadas.

# Exemplo de Entrada:

# Digite o texto a ser revisado: O dia está bom, tudo está bom.`
# Qual palavra deseja substituir? bom
# Qual a nova palavra? ótimo

# Saída esperada:

# O dia está ótimo, tudo está ótimo.
