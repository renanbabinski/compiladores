from TipoToken import TipoToken

class Token:
    # nome = TipoToken()
    # lexema = ""

    def __init__(self, nome, lexema):
        self.nome = TipoToken(nome).name
        self.lexema = lexema

    def __str__(self):

        return str(self.nome)+' '
    
    def get_token(self):
        return self.nome, self.lexema