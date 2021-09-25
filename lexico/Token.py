import TipoToken

class Token:
    # nome = TipoToken()
    # lexema = ""

    def __init__(self, nome, lexema):
        self.nome = TipoToken(nome)
        self.lexema = lexema

    def __str__(self):
        return "<"+self.nome+","+self.lexema+">"
    