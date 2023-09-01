# Função para avaliar uma expressão em notação prefixa
def avaliar_expressao(expressao):
    pilha = []  # Pilha para armazenar os operandos e resultados intermediários

    operadores = set(['+', '-', '*', '/'])  # Conjunto de operadores válidos

    tokens = expressao.split()  # Divide a expressão em tokens
    tokens.reverse()  # Inverte a ordem dos tokens para avaliar da direita para a esquerda

    for token in tokens:
        if token not in operadores:
            pilha.append(int(token))  # Empilha os operandos na pilha
        else:
            operando1 = pilha.pop()
            operando2 = pilha.pop()

            # Realiza a operação com base no operador atual
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            else:  # token == '/'
                resultado = int(operando1 / operando2)

            pilha.append(resultado)  # Empilha o resultado intermediário

    return pilha[0]  # Retorna o resultado final da expressão

# Lista para armazenar as expressões
arm_expressoes = []

# Loop para ler as expressões da entrada até que uma entrada vazia seja fornecida
while True:
    try:
        expressao = input()
        if not expressao:
            raise EOFError
        arm_expressoes.append(expressao)
    except EOFError:
        break

# Avalia cada expressão e armazena os resultados em uma lista
resultados = [avaliar_expressao(expr) for expr in arm_expressoes]

# Exibe os resultados na saída
for resultado in resultados:
    print(resultado)