from random import randint

class Player():
    def __init__(self):
        self.nome = None
        self.classe = None
        self.vida = None
        self.ataque = None
        self.defesa = None

    def rolar_dados(self):
        return randint(0, 10) * 10

    def atacar(self, alvo):
        dados_ataque = self.rolar_dados()
        dados_defesa = alvo.rolar_dados()
        if dados_ataque == 0:
            print('Você errou..')
            return
        ataque = self.ataque * dados_ataque/100
        defesa = alvo.ataque * dados_defesa/100
        dano = ataque - (ataque * defesa/100)
        alvo.vida -= dano