def maior_valor_mochila(comprimentos, valores, capacidade):
    n_itens = len(comprimentos)
    T = [[0 for j in range(capacidade + 1)] for i in range(n_itens + 1)]

    for j in range(1, capacidade + 1):
        for i in range(1, n_itens + 1):
            if comprimentos[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], T[i - 1][j - comprimentos[i - 1]] + valores[i - 1])

    return T[n_itens][capacidade]

# Entrada do usuário
n, capacidade = map(int, input().split())
tamanhos = []
valores = []

for _ in range(n):
  tam, val = map(int, input().split())
  tamanhos.append(tam)
  valores.append(val)

# Chamar a função e imprimir o resultado
resultado = maior_valor_mochila(tamanhos, valores, capacidade)
print(resultado)
