from time import sleep
from .Classes.class_guerreiro import Guerreiro 
from .Classes.class_assassino import Assassino
from .Classes.class_tanque import Tanque
from .player import Player
from os import system
import keyboard
import getpass
from random import randint

def limpa_tela():
    system('cls')

class Jogo():
    def __init__(self):
        limpa_tela()
        self.player1 = Player()
        self.player2 = Player()
        self.mostra_titulo('Bem vindo ao jogo de luta!')

    def espera_entradas(self, *teclas):
        teclas = list(map(str, teclas))
        tecla = keyboard.read_key()
        if tecla in teclas:
            return tecla

    def mostra_titulo(self, txt):
        mensagem = txt
        print('-='* (len(mensagem)//2))
        print(mensagem)
        print('-='* (len(mensagem)//2))

    def descricao_classe(self, classe):
        print('-='*10)
        print(f'Classe: {classe.atributos["classe"]}')
        print(f'Vida  : {classe.atributos["vida"]}')
        print(f'Ataque: {classe.atributos["ataque"]}')
        print(f'Defesa: {classe.atributos["defesa"]}')
        print('-='*10)

    def selecionar_classe(self, nome):
        i = 0
        escolheu = False
        classe_selecionada = None
        sleep(.25)
        print('Selecione a sua Classe')
        while True: 
            limpa_tela()
            self.mostra_titulo('Bem vindo ao jogo de luta!')
            print(nome+',')
            print('Selecione sua Classe:')
            if i == -1:
                self.descricao_classe(Tanque())
                classe_selecionada = Tanque()
                i = 2
            elif i == 0:
                self.descricao_classe(Guerreiro())
                classe_selecionada = Guerreiro()
            elif i == 1:
                self.descricao_classe(Assassino())
                classe_selecionada = Assassino()
            elif i == 2:
                self.descricao_classe(Tanque())
                classe_selecionada = Tanque()
            elif i == 3:
                self.descricao_classe(Guerreiro())
                classe_selecionada = Guerreiro()
                i = 0

            print('''Proxima Classe [->]
Volta Classe [<-]
Selecionar Classe [Enter]''')

            if i in (0, 1, 2):
                while True:
                    tecla = keyboard.read_key()
                    if tecla == 'enter':
                        escolheu = True
                        break
                    if tecla == 'left' or tecla == 'down':
                        i -= 1
                        sleep(.25)
                        break
                    if tecla == 'right' or tecla == 'up':
                        i += 1
                        sleep(.25)
                        break
            if escolheu:
                getpass.getpass('')
                break      
                    
        return classe_selecionada
    
    def criar_jogadores(self):
        jogadores = (self.player1, self.player2)
        for i, jogador in enumerate(jogadores):
            limpa_tela()
            self.mostra_titulo('Bem vindo ao jogo de luta!')
            print('Jogador', i+1)
            jogador.nome = input('Digite seu nome: ')
            jogador.classe = self.selecionar_classe(jogador.nome)
            jogador.vida = jogador.classe.atributos['vida']
            jogador.ataque = jogador.classe.atributos['ataque']
            jogador.defesa = jogador.classe.atributos['defesa']
            print(f'\nClasse Selecionada: {jogador.classe.atributos["classe"]}\n')
            sleep(1.3)

    def teste(self,origem, destino):
        origem = destino

    def luta(self):
        players = [self.player1, self.player2]
        oponentes = [self.player2, self.player1]
        for player, oponente in players, oponentes:
            limpa_tela()
            print(f'''{player.nome},
Escolha uma ação:
1 - Atacar
2 - Fugir
0 - Encerrar o jogo''')
            acao = int(self.espera_entradas(0, 1, 2))
            match acao:
                case 1:
                    player.atacar(oponente)
                case 2:
                    player.fugir()
                case 0:
                    self.finaliza_jogo()
            self.mostra_status_batalha()
            if self.player1.vida <= 0 or self.player2.vida <= 0:
                return

    def mostra_status_batalha(self):
        vida  = 'Vida: '+ str(self.player1.vida)
        vida2 = 'Vida: '+ str(self.player2.vida)
        self.mostra_titulo('Resumo da Batalha')
        print(f"{self.player1.nome:20}{self.player2.nome}")
        print(f"{vida:20}{vida2}")
        sleep(2)
        print('Pressione Enter para Continuar...')
        self.espera_entradas('enter')
        
    def main(self):
        self.criar_jogadores()
        limpa_tela()
        print('Vamos Começar!')
        sleep(1.25)
        self.luta()
        

if __name__ == "__main__":
    jogo = Jogo()
    jogo.main()