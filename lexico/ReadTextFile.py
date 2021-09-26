class ReadTextFile:
    BUFFER = 5
    def __init__(self, arquivo):
        self.buffer = [None]*__class__.BUFFER
        self.pointer = __class__.BUFFER-1
        try:
            self.f = open(arquivo, 'r', encoding='utf-8')
        except FileNotFoundError:
            print("file {} does not exist".format(arquivo))
            exit()
        
    def readNextCharacter(self):
        #print(self.buffer)
        character = self.f.read(1)
        if not character:
            return -1
        self.buffer.append(character)
        del(self.buffer[0])
        c = self.buffer[self.pointer]
        if self.pointer != __class__.BUFFER-1:
            self.pointer += 1
        print(c, end='')
        return c

    def go_back_buffer(self):
        self.pointer -= 1