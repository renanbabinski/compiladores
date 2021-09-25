class ReadTextFile:
    def __init__(self, arquivo):
        try:
            self.f = open(arquivo, 'r')
        except FileNotFoundError:
            print("file {} does not exist".format(arquivo))
        
    def readNextCharacter(self):
        #with self.f:
        character = self.f.read(1)
        #print(type(character))
        if not character:
            #print("End of file")
            return -1
        print(character, end='')
        return character
        