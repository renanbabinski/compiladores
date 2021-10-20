import json
from os import stat


# Arquivos de entrada

with open(r'C:\Users\Renan\Documents\GitHub\compiladores\syntatic\input_json\grammar.json', 'r', encoding='utf-8') as file:
    grammar = json.load(file)

with open(r'C:\Users\Renan\Documents\GitHub\compiladores\syntatic\input_json\slr_table.json', 'r', encoding='utf-8') as file:
    slr = json.load(file)

with open(r'C:\Users\Renan\Documents\GitHub\compiladores\lexico\tokens_output\tokens.json', 'r', encoding='utf-8') as file:
    tokens = json.load(file)

#####################FUNCTIONS#############################

def print_steps(step, pilha, fluxo_tokens):
    step += 1
    print('-------------------')
    print('STEP -> {}\nPILHA -> {}\nENTRADA -> {}'.format(step, pilha, fluxo_tokens))
    print('-------------------')
    return step


###########################################################
step = 0

fluxo_tokens = []
for token in tokens['TOKENS']:
    fluxo_tokens.append(token['nome'])

fluxo_tokens.append('$')
#print(fluxo_tokens)

pilha = ['0']
reduce = False
#print(pilha)

# Enquanto a transição não for 'acc' e nem ' ' esse loop executará
while True:
    # Quando houver uma redução não preciso mostrar os steps novamente
    if not reduce:
        step = print_steps(step, pilha, fluxo_tokens)

    token = fluxo_tokens[0]
    state = pilha[-1]
    new_state = slr['ACTIONS'][token][int(state)]['action']
    if new_state[0] == 's':
        print('SHIFT')

        pilha.append(token)
        pilha.append(new_state[1:])
        fluxo_tokens.pop(0)

        reduce = False

    elif new_state[0] == 'r':
        print('REDUCE')

        production_index = int(new_state[1:])
        reduce_len = len(grammar['GRAMMAR'][production_index]['body'].split(' '))
        reduce_len = reduce_len * 2
        print('TAMANHO DA REDUÇÃO: {}'.format(reduce_len))
        
        for i in range(reduce_len):
            pilha.pop()

        token = grammar['GRAMMAR'][production_index]['head']
        state = pilha[-1]
        new_state = slr['GOTO'][token][int(state)]['goto']


        pilha.append(token)
        step = print_steps(step, pilha, fluxo_tokens)

        pilha.append(new_state)
        step = print_steps(step, pilha, fluxo_tokens)

        reduce = True        
        
    elif new_state == 'acc':
        print("######\nPROGRAMA CORRETO\n#########")
        break
        

    else:
        print("ERRO SINTÁTICO")
        print("Na linha {}".format())
        print("Expected {}".format(pilha[-2]))
        break


