from TipoToken import TipoToken
from Lexico import Lexico
import json
import time
import os

# Programa de entrada 
lex = Lexico(r'C:\Users\Renan\Documents\GitHub\compiladores\input_programs\programa_com_erro.txt')
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
    nome, lexema, line = t.get_token()
    if str(nome) in op_rel:
        # cria um token único para operador relacional = OpRel
        nome = 'OpRel'
        print('OpRel', end=' ')
    else:
        print(t, end='')
    
    new_token = {'nome': nome, 'lexema': lexema, 'linha': line}
    tokens['TOKENS'].append(new_token)

# Arquivo de saída estruturado com os tokens
file = r"C:\Users\Renan\Documents\GitHub\compiladores\lexico\tokens_output\tokens.json"
os.makedirs(os.path.dirname(file), exist_ok=True)
with open(file, 'w', encoding='utf-8') as wfile:
    json.dump(tokens, wfile, ensure_ascii=False, indent=4)




