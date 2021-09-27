class ReadTextFile:
    BUFFER = 20
    def __init__(self, arquivo):
        self.buffer = [None]*__class__.BUFFER
        self.pointer = __class__.BUFFER-1
        self.lexeme_init = 0
        self.lexeme = ""
        try:
            self.f = open(arquivo, 'r', encoding='utf-8')
        except FileNotFoundError:
            print("file {} does not exist".format(arquivo))
            exit()
        
    def readNextCharacter(self):
        if self.pointer == __class__.BUFFER-1:
            character = self.f.read(1)
            if not character:
                return -1
            self.buffer.append(character)
            del(self.buffer[0])
            c = self.buffer[self.pointer]
        else:
            self.pointer += 1
            c = self.buffer[self.pointer]
        print(c, end='')
        self.lexeme += c
        print(self.lexeme)
        #print(self.buffer)
        return c

    def go_back_buffer(self):
        self.pointer -= 1
        self.lexeme = self.lexeme[0:-1]

    def reset(self):
        self.pointer = self.lexeme_init
        self.lexeme = ""

    def confirm(self):
        self.lexeme_init = self.pointer
        self.lexeme = ""

    def get_lexema(self):
        return self.lexeme