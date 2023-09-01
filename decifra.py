alfabeto_modificado = input()
frase_desejada = input()

nova_frase = ""

for letra in frase_desejada:
    indice = ord(letra) - ord('a')
    correspondente = alfabeto_modificado[indice]
    nova_frase += correspondente

print(nova_frase)