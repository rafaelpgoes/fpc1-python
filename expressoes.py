def esta_bem_definida(expressao):
    caracteres_abertura = {'{': '}', '[': ']', '(': ')'}
    fila = []

    for char in expressao:
        if char in caracteres_abertura:
            fila.append(char)
        elif char in caracteres_abertura.values():
            if not fila or caracteres_abertura[fila[-1]] != char:
                return False
            fila.pop()
    
    return len(fila) == 0

# Leitura do número de instâncias
T = int(input())
entradas = []

# Coleta de todas as instâncias de entrada
for _ in range(T):
    expressao = input().strip()
    entradas.append(expressao)

# Processamento e impressão dos resultados
for expressao in entradas:
    resultado = 'S' if esta_bem_definida(expressao) else 'N'
    print(resultado)
