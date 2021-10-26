class Tanque():
    def __init__(self):
        self.atributos = {
            "classe":'Tanque',
            "vida": 200,
            "ataque": 10,
            'defesa': 50
        }
        from .class_assassino import Assassino
        from .class_guerreiro import Guerreiro