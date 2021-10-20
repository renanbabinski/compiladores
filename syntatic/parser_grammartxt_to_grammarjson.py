## Author: Renan Luiz Babinski
## Este programa faz o parsing da gramática (como adicionada no site) http://jsmachines.sourceforge.net/machines/slr.html para um arquivo JSON


import json
import os


grammar = {'GRAMMAR':[]}

#Arquivo TXT de entrada
with open(r'C:\Users\Renan\Documents\GitHub\compiladores\grammar\grammar.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line, num_line in zip(lines, range(len(lines))):
        #remove a quebra de linha do final da string
        line = line[0:-1]
        #quebra os valores da tabela conforme a tabulação
        line = line.split('->')
        #Remove espaços em branco
        for index in range(len(line)):
            line[index] = line[index].strip(' ')
        print(line)

        new_production = {'prod_number': num_line, 'head': line[0], 'body': line[1]}
        grammar['GRAMMAR'].append(new_production)
           

#Arquivo JSON de saída
file = r"C:\Users\Renan\Documents\GitHub\compiladores\syntatic\input_json\grammar.json"
os.makedirs(os.path.dirname(file), exist_ok=True)
with open(file, 'w', encoding='utf-8') as wfile:
    json.dump(grammar, wfile, ensure_ascii=False, indent=4)
