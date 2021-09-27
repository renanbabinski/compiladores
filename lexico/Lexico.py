from Token import Token
from TipoToken import TipoToken
from ReadTextFile import ReadTextFile

class Lexico:
    def __init__(self, arquivo):
        self.ldat = ReadTextFile(arquivo)

    def next_token(self):
        c = "@"
        c.is

        while(c != -1):
            c = self.ldat.readNextCharacter()
            if(c == ' ' or c == '\n'):
                continue

        return None

    def arithmetic_operator(self):
        c = self.ldat.readNextCharacter()
        if c == '*':
                return Token(TipoToken.OpAritMult, self.ldat.get_lexema())
        elif c == '/':
            return Token(TipoToken.OpAritDiv, self.ldat.get_lexema())
        elif c == '+':
            return Token(TipoToken.OpAritSum, self.ldat.get_lexema())
        elif c == '-':
            return Token(TipoToken.OpAritSub, self.ldat.get_lexema())
        else:
            return None

    def delimiter(self):
        c = self.ldat.readNextCharacter()
        if c == ':':
                return Token(TipoToken.Delim, self.ldat.get_lexema())
        else:
            return None

    def relational_operator(self):
        c = self.ldat.readNextCharacter()
        if c == '<':
            c = self.ldat.readNextCharacter()
            if c == '>':
                return Token(TipoToken.OpRelDiff, self.ldat.get_lexema())
            elif c == '=':
                return Token(TipoToken.OpRelSmallerEqual, self.ldat.get_lexema())
            else:
                self.ldat.go_back_buffer()
                return Token(TipoToken.OpRelSmaller, self.ldat.get_lexema())
        elif c == '=':
            return Token(TipoToken.OpRelEqual, self.ldat.get_lexema())
        elif c == '>':
            c = self.ldat.readNextCharacter()
            if c == '=':
                return Token(TipoToken.OpRelBiggerEqual, self.ldat.get_lexema())
            else:
                self.ldat.go_back_buffer()
                return Token(TipoToken.OpRelBigger, self.ldat.get_lexema())
        else:
            return None

    def parentheses(self):
        c = self.ldat.readNextCharacter()
        if c == '(':
            return Token(TipoToken.OpenPar, self.ldat.get_lexema())
        elif c == ')':
            return Token(TipoToken.ClosePar, self.ldat.get_lexema())
        else:
            return None

    def numbers(self):
        state = 1
        while True:
            c = self.ldat.readNextCharacter()
            if state == 1:
                if c.isdigit():
                    state = 2
                else:
                    return None
            elif state == 2:
                if c == '.':
                    c = self.ldat.readNextCharacter()
                    if c.isdigit():
                        state = 3
                    else:
                        return None
                elif not c.isdigit():
                    self.ldat.go_back_buffer()
                    return Token(TipoToken.NumInt, self.ldat.get_lexema())
            elif state == 3:
                if not c.isdigit():
                    self.ldat.go_back_buffer()
                    return Token(TipoToken.NumReal, self.ldat.get_lexema())

    def variable(self):
        state = 1
        while True:
            c = self.ldat.readNextCharacter()
            if state == 1:
                if 
