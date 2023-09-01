#função de soma
def soma(lista):
    s = 0
    for i in lista:
        s += i
    return s

#lendo entradas
n_colunas = int(input())
colunas = [int(i) for i in input().split()]
n_pedras = sum(colunas)
n_pedras_escada = int(n_colunas * (n_colunas + 1) / 2)

if (n_pedras - n_pedras_escada) % n_colunas != 0:
    print(-1)
else:
    #laço dos movimentos
    base = int((n_pedras - n_pedras_escada) / n_colunas)
    n_movimentos = 0 
    for idx, coluna in enumerate(colunas):
        if coluna > base + idx + 1: #representa oque preciso
            n_movimentos += coluna - (base + idx + 1)
    print(n_movimentos)