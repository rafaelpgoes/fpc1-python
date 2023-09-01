# Utilização da implementação de fila feita em sala
class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.prox = None
        self.ant = None

    def __str__(self):
        return f"Meu querido dado:{self.dado}"

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def is_vazia(self):
        return self.inicio is None or self.fim is None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.ant = self.fim
            self.fim.prox = novo_no
            self.fim = novo_no

    def remover(self):
        if self.is_vazia():
            return None
        valor = self.inicio.dado
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.prox
            self.inicio.ant = None
        return valor

def contar_pares_corretos(fila_botas):
    pares_corretos = 0
    bota_dicionario = {}

    while not fila_botas.is_vazia():
        bota = fila_botas.remover().split()
        tamanho, pe = int(bota[0]), bota[1]
        
        if tamanho not in bota_dicionario:
            bota_dicionario[tamanho] = [0, 0]  # [Esquerda, Direita]
        
        if pe == 'E':
            bota_dicionario[tamanho][0] += 1
        elif pe == 'D':
            bota_dicionario[tamanho][1] += 1

    for tamanho in bota_dicionario:
        pares_corretos += min(bota_dicionario[tamanho])

    return pares_corretos

# Leitura da entrada
n = int(input())
fila_botas_entregues = Fila()
for _ in range(n):
    bota = input()
    fila_botas_entregues.inserir(bota)

# Chamada da função e impressão do resultado
resultado = contar_pares_corretos(fila_botas_entregues)
print(resultado)