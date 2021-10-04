from TipoToken import TipoToken
from Lexico import Lexico
import json
import time


lex = Lexico(r'C:\Users\Renan\Documents\GitHub\compiladores\lexico\programa.txt')
t = True
tokens = {'TOKENS':[]}
op_rel = ['OpRelSmaller',
          'OpRelSmallerEqual',
          'OpRelBigger',
          'OpRelBiggerEqual',
          'OpRelEqual',
          'OpRelDiff']


while True:
    t = lex.next_token()
    if t.lexema == 'Fim':
        break
    print(t, end='')
    nome, lexema = t.get_token()
    # cria um token único para operador relacional = OpRel
    if str(nome) in op_rel:
        nome = 'OpRel'
    new_token = {'nome': nome, 'lexema': lexema}
    tokens['TOKENS'].append(new_token)
    time.sleep(0.1)

with open(r'C:\Users\Renan\Documents\GitHub\compiladores\lexico\tokens.json', 'w', encoding='utf-8') as wfile:
    json.dump(tokens, wfile, ensure_ascii=False, indent=4)




