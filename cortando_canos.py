def maior_valor_corte_canos(n, tamanho_tubo, comprimentos, valores):
    T = [0] * (tamanho_tubo + 1)

    for j in range(1, tamanho_tubo + 1):
        for i in range(n):
            if comprimentos[i] <= j:
                T[j] = max(T[j], T[j - comprimentos[i]] + valores[i])

    return T[tamanho_tubo]

# Leitura da entrada do usuário
n, tamanho_tubo = map(int, input().split())
comprimentos = []
valores = []

for _ in range(n):
    tam, val = map(int, input().split())
    comprimentos.append(tam)
    valores.append(val)

resultado = maior_valor_corte_canos(n, tamanho_tubo, comprimentos, valores)
print(resultado)
