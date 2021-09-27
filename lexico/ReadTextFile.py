class ReadTextFile:
    BUFFER = 20
    def __init__(self, arquivo):
        self.buffer = [None]*__class__.BUFFER
        self.pointer = __class__.BUFFER-1
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
        #print(self.buffer)
        return c

    def go_back_buffer(self):
        self.pointer -= 1