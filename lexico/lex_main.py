from Lexico import Lexico


lex = Lexico('/home/anonymous/GitHub/compiladores/lexico/programa.txt')
t = True


while True:
    t = lex.next_token()
    if t == None:
        break

print()
