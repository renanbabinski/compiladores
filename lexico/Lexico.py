from ReadTextFile import ReadTextFile

class Lexico:
    def __init__(self, arquivo):
        self.ldat = ReadTextFile(arquivo)

    def next_token(self):
        readed_character = " "

        while(readed_character != -1):
            readed_character = self.ldat.readNextCharacter()
            if(readed_character == ' ' or readed_character == '\n'):
                continue

        return None