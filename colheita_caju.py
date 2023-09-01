# código corrigido
def maxima_colheita(L, C, M, N, fazenda):
    # Utilização de memoização, assim como descrito no cormen, para evitar
    # repetição de sequências ao analizar quadrantes de procura
    memoizacao = {}

    # Função interna para calcular a colheita em uma coordenada (i, j)
    def calcular_colheita(i, j):
        # Verifica se a coordenada já foi calculada antes
        if (i, j) in memoizacao:
            return memoizacao[(i, j)]

        colheita_atual = 0
        # Calcula o quadrante atual
        for k in range(i, i + M):
            for l in range(j, j + N):
                colheita_atual += fazenda[k][l]

        # Armazena o resultado da colheita no dicionário de memoização
        memoizacao[(i, j)] = colheita_atual
        return colheita_atual

    maxima_colheita = 0

    # Percorre coordenadas
    for i in range(L - M + 1):
        for j in range(C - N + 1):
            colheita_atual = calcular_colheita(i, j)
            maxima_colheita = max(maxima_colheita, colheita_atual)

    return maxima_colheita

# Leitura da entrada
L, C, M, N = map(int, input().split())
fazenda = []
for _ in range(L):
    linha = list(map(int, input().split()))
    fazenda.append(linha)

# Chamada da função e impressão da saída
resultado = maxima_colheita(L, C, M, N, fazenda)
print(resultado)