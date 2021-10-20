## Author: Renan Luiz Babinski
## Este programa faz o parsing da tabela SLR gerada no site http://jsmachines.sourceforge.net/machines/slr.html para um arquivo JSON
## IMPORTANTE: Onde há conflito shift-reduce (em vermelho na tabela do site), deve se remover o shift manualmente do arquivo txt que será convertido


import json
import os

lr_table = dict()

#Arquivo TXT de entrada
with open(r'C:\Users\Renan\Documents\GitHub\compiladores\syntatic\input_txt\slr_table.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line, num_line in zip(lines, range(len(lines))):
        #remove a quebra de linha do final da string
        line = line[0:-1]
        #quebra os valores da tabela conforme a tabulação
        line = line.split('\t')
        if num_line == 0:
            continue
        elif num_line == 1:
            lr_table = {"ACTIONS": {}, "GOTO": {}}
        elif num_line == 2:
            goto = False
            for head in line:
                if not goto:
                    lr_table['ACTIONS'][head] = []
                else:
                    lr_table['GOTO'][head] = []
                if head == '$':
                    goto = True
        else:
            state = line[0]
            for key, index in zip(lr_table['ACTIONS'].keys(), range(1, len(lr_table['ACTIONS'])+1)):
                new_action = {'state': state, 'action': line[index]}
                lr_table['ACTIONS'][key].append(new_action)

            for key, index in zip(lr_table['GOTO'].keys(), range(len(lr_table['ACTIONS'])+1, (len(lr_table['ACTIONS'])+1) + (len(lr_table['GOTO'])))):
                new_action = {'state': state, 'goto': line[index]}
                lr_table['GOTO'][key].append(new_action)
           

#Arquivo JSON de saída
file = r"C:\Users\Renan\Documents\GitHub\compiladores\syntatic\input_json\slr_table.json"
os.makedirs(os.path.dirname(file), exist_ok=True)
with open(file, 'w', encoding='utf-8') as wfile:
    json.dump(lr_table, wfile, ensure_ascii=False, indent=4)

