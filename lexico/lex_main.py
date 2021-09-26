from Lexico import Lexico


lex = Lexico(r'C:\Users\Renan\Documents\GitHub\compiladores\lexico\programa.txt')
t = True


while True:
    t = lex.next_token()
    if t == None:
        break
    print(t, end='')

print()
