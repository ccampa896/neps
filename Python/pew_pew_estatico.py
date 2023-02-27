class Inimigo:

    quantidade_vivos = 0

    # TODO: Crie um construtor que inicializa um inimigo usando os parâmetros abaixo.
    def __init__(self, id: int, X: int, Y: int, vivo: bool):
        self.id = id
        self.X = X
        self.Y = Y
        self.vivo = vivo
        Inimigo.quantidade_vivos += 1

    # TODO: Método que muda a o status do inimigo de vivo para morto caso seja acertado pelo lazer na posição (X,Y). Também deve atualizar a variável quantidade_vivos.
    def foi_acertado(self, X: int, Y: int) -> None:
        if self.X == X and self.Y == Y:
            if self.vivo == False:
                return
            else:
                self.vivo = False
                Inimigo.quantidade_vivos -= 1



if __name__ == "__main__":

    n = int(input())

    inimigos = []


    for id in range(n):
        x, y = map(int, input().split())
        inimigos.append(Inimigo(id, x, y, True))

    m = int(input())

    for i in range(m):
        x, y = map(int, input().split())

        for inimigo in inimigos:
            inimigo.foi_acertado(x, y)

    print(f'vivos: {Inimigo.quantidade_vivos}')
    print(f'mortos: {n - Inimigo.quantidade_vivos}')

