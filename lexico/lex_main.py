from TipoToken import TipoToken
from Lexico import Lexico
import json
import time


lex = Lexico(r'/home/anonymous/GitHub/compiladores/lexico/programa2.txt')
t = True
tokens = {'TOKENS':[]}


while True:
    t = lex.next_token()
    if t.lexema == 'Fim':
        break
    print(t, end='')
    nome, lexema = t.get_token()
    new_token = {'nome': nome, 'lexema': lexema}
    tokens['TOKENS'].append(new_token)
    time.sleep(0.2)

with open(r'/home/anonymous/GitHub/compiladores/lexico/tokens2.json', 'w', encoding='utf-8') as wfile:
    json.dump(tokens, wfile, ensure_ascii=False, indent=4)




