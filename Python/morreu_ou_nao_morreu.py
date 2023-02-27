class Personagem:
    def __init__(self, nome: str, ataque: int, defesa: int, vida: int):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida

    # Crie um método que determina se o personagem morreu ou não após receber o golpe.
    def sobreviveu(self, dano):
        if (dano - defesa) >= vida:
            return False
        return True

if __name__ == "__main__":

    nome = input()
    ataque = int(input())
    defesa = int(input())
    vida = int(input())

    personagem = Personagem(nome, ataque, defesa, vida)

    dano = int(input())

    if personagem.sobreviveu(dano):
        print(f"{personagem.nome} sobreviveu!!!")
    else:
        print(f"{personagem.nome} morreu :(")

