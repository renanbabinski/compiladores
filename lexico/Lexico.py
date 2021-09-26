from Token import Token
from TipoToken import TipoToken
from ReadTextFile import ReadTextFile

class Lexico:
    def __init__(self, arquivo):
        self.ldat = ReadTextFile(arquivo)

    def next_token(self):
        c = " "

        while(c != -1):
            c = self.ldat.readNextCharacter()
            if(c == ' ' or c == '\n'):
                continue
            if c == ':':
                return Token(TipoToken.Delim, ':')
            elif c == '*':
                return Token(TipoToken.OpAritMult, '*')
            elif c == '/':
                return Token(TipoToken.OpAritDiv, '/')
            elif c == '+':
                return Token(TipoToken.OpAritSum, '+')
            elif c == '-':
                return Token(TipoToken.OpAritSub, '-')
            elif c == '(':
                return Token(TipoToken.OpenPar, '(')
            elif c == ')':
                return Token(TipoToken.ClosePar, ')')
            elif c == '<':
                c = self.ldat.readNextCharacter()
                if c == '>':
                    return Token(TipoToken.OpRelDiff, '<>')
                elif c == '=':
                    return Token(TipoToken.OpRelSmallerEqual, '<=')
                else:
                    self.ldat.go_back_buffer()
                    return Token(TipoToken.OpRelSmaller, '<')
                
            

        return None