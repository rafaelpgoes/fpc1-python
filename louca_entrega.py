class Baralho:
    def __init__(self, ID, deck=None):
        self.ID = ID
        self.cartas = deck or []

    def retirar_carta_jogador(self):
        del self.cartas[0]

    def colocar_no_final(self):
        self.cartas.append(self.cartas.pop(0))

def main():
    numero_de_festas = int(input())

    if not 0 < numero_de_festas <= 10**5:
        return

    vencedores = []

    for _ in range(numero_de_festas):
        jogadores = [Baralho(i, input().split()) for i in range(1, int(input()) + 1)]
        deck_mesa = Baralho(0, input().split())
        carta_atual = deck_mesa.cartas[0]

        for n_de_rodadas in range(1, 1001):
            empatados = [jogador for jogador in jogadores if jogador.cartas and jogador.cartas[0] == carta_atual]

            if len(empatados) == 1 or n_de_rodadas == 1000:
                vencedores.append(empatados[0] if len(empatados) == 1 else Baralho(0))  # Juvenal
                break
            elif len(empatados) > 1:
                vencedores.append(min(empatados, key=lambda x: x.ID))
                break

            for jogador in jogadores:
                if jogador.cartas and jogador.cartas[0] != carta_atual:
                    jogador.colocar_no_final()
                else:
                    jogador.retirar_carta_jogador()

            deck_mesa.colocar_no_final()
            carta_atual = deck_mesa.cartas[0]

    for vencedor in vencedores:
        print(vencedor.ID)

if __name__ == "__main__":
    main()