from os import stat
from Token import Token
from TipoToken import TipoToken
from ReadTextFile import ReadTextFile

class Lexico:
    def __init__(self, arquivo, DEBUG=False):
        self.ldat = ReadTextFile(arquivo)
        self.debug = DEBUG

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
                if c.isalpha():
                    state = 2
                else:
                    return None
            elif state == 2:
                if not c.isalnum():
                    self.ldat.go_back_buffer()
                    return Token(TipoToken.Var, self.ldat.get_lexema())

    def string(self):
        state = 1
        while True:
            c = self.ldat.readNextCharacter()
            if state == 1:
                if c == '\'':
                    state = 2
                else:
                    return None
            elif state == 2:
                if c == '\n':
                    return None
                if c == '\'':
                    return Token(TipoToken.String, self.ldat.get_lexema())
                elif c == '\\':
                    state = 3
            elif state == 3:
                if c == '\n':
                    return None
                else:
                    state = 2

    def spaces_and_comments(self):
        state = 1
        while True:
            c = self.ldat.readNextCharacter()
            if c == -1:
                return Token(TipoToken.End, 'Fim')
            if state == 1:
                if c.isspace() or c == ' ':
                    state = 2
                elif c == '%':
                    state = 3
                else:
                    self.ldat.go_back_buffer()
                    return
            elif state == 2:
                if c == '%':
                    state = 3
                elif not (c.isspace() or c == ' '):
                    self.ldat.go_back_buffer()
                    return
            elif state == 3:
                if c == '\n':
                    self.ldat.readNextCharacter()
                    self.ldat.confirm()
                    return

    def key_words(self):
        while True:
            c = self.ldat.readNextCharacter()
            if not c.isalpha():
                self.ldat.go_back_buffer()
                lexema = ""
                lexema = self.ldat.get_lexema()
                if lexema == 'STATEMENTS':
                    return Token(TipoToken.KwStatements, lexema)
                elif lexema == 'ALGORITHM':
                    return Token(TipoToken.KwAlgorithm, lexema)
                elif lexema == 'INT':
                    return Token(TipoToken.KwInteger, lexema)
                elif lexema == 'REAL':
                    return Token(TipoToken.KwReal, lexema)
                elif lexema == 'ASSIGN':
                    return Token(TipoToken.KwAssign, lexema)
                elif lexema == 'TO':
                    return Token(TipoToken.KwTo, lexema)
                elif lexema == 'READ':
                    return Token(TipoToken.KwRead, lexema)
                elif lexema == 'PRINT':
                    return Token(TipoToken.KwPrint, lexema)
                elif lexema == 'IF':
                    return Token(TipoToken.KwIf, lexema)
                elif lexema == 'ELSE':
                    return Token(TipoToken.KwElse, lexema)
                elif lexema == 'THEN':
                    return Token(TipoToken.KwThen, lexema)
                elif lexema == 'WHILE':
                    return Token(TipoToken.KwWhile, lexema)
                elif lexema == 'BEGIN':
                    return Token(TipoToken.KwBegin, lexema)
                elif lexema == 'END':
                    return Token(TipoToken.KwEnd, lexema)
                elif lexema == 'AND':
                    return Token(TipoToken.OpBoolAnd, lexema)
                elif lexema == 'OR':
                    return Token(TipoToken.OpBoolOr, lexema)
                else:
                    return None

    def end(self):
        c = self.ldat.readNextCharacter()
        if c == -1:
            return Token(TipoToken.End, 'Fim')
        return None
                
    def next_token(self):
        next = None
        try_number = 0

        try_number += 1
        if self.debug:
            print("{} - TRY SPACES AND COMMENTS PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.spaces_and_comments()
        if next != None:
            if next.nome == TipoToken.End:
                return Token(TipoToken.End, 'Fim')
        self.ldat.confirm()

        try_number += 1
        if self.debug:
            print("{} - TRY END PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.end()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY KEYWORDS PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.key_words()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY VARIABLE PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.variable()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY NUMBERS PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.numbers()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY ARITHMETIC OPERATOR PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.arithmetic_operator()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next
        
        try_number += 1
        if self.debug:
            print("{} - TRY RELATIONAL OPERATOR PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.relational_operator()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY DELIMITER PATTERN:".format(try_number))
            self.ldat.print_buffer()
        
        next = self.delimiter()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY PARENTHESES PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.parentheses()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        try_number += 1
        if self.debug:
            print("{} - TRY STRING PATTERN:".format(try_number))
            self.ldat.print_buffer()

        next = self.string()
        if next == None:
            self.ldat.reset()
        else:
            self.ldat.confirm()
            return next

        print('Erro léxico!')

        return None

