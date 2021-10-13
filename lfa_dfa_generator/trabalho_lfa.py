"""Programa para GERAR AFND, AFD, ELIMINAR MORTOS E INALCANÇÁVEIS
Criado por Darlan Adriano Schmitz
Modificado por Renan Luiz Babinski
Ciencias da Computação - UFFS"""

import os
import sys
import string

so = sys.platform                                                               # Pega qual é o SO
so_clear = ''

if (so == 'linux'):                                                             # Defini o argumento para limpeza de tela de acordo com o SO
    so_clear = 'clear'
elif (so[:3] == 'win'):
    so_clear = 'cls'

if so_clear:                                                                    # Função lambda para limpeza de tela
    limpar = lambda l: os.system(l)
else:
    limpar = lambda l: l

def main():                                                                     #função main
    limpar(so_clear)
    existe()
    try:
        file = open('entrada.txt','r')
        file.seek(0,0)
        lista_nome_gramatica = []                                               #Lista para armazenar as regras das grámaticas
        lista_producao_gramatica = []                                           #lista para armazenar as produções das gramatica
        lista_producao_token = []                                               #lista para armazenar as produções dos tokens
        lista_elementos_terminais = []                                          #lista para armazenar os elementos terminais
        lista_elementos_producao_all = []                                       #lista para produção dos tokens e gramáticas
        alpha_lower = list(string.ascii_lowercase)
        alpha_upper = list(string.ascii_uppercase)
        lista_gramaticas_end = []                                               #lista para armazenar os elementos que dão nomes às gramáticas e são terminais
        lista_prod_x_gramatica = []                                             #lista para pegara a produção de uma unica regra

        for line in file:                                                       #for para andar no arquivo
            #print(line.strip())
            if line[0] == '<':                                                  #se for gramatica vai entrar aqui Verifica se o primeiro elemento da linha é <
                #print('É gramatica')
                count = 0                                                       #contador que será usado para pegar as letras nos araquivos
                for letra_gramatica in line:                                    #for para andar caracter por caracter no arquivo
                    if letra_gramatica == '<':                                  #qaundo tiver esse caracter a próxima letra sera Uma letra que dá nome a gramatica
                        tem = nao_repetir(lista_nome_gramatica,line[count+1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_nome_gramatica.append(line[count+1])           #escreve a letra que da nome à gramatica
                        #print(letra_gramatica)

                    if letra_gramatica == '<' and count != 0 :                  #se for o primeiro simbolo add a lista de produções
                        tem = nao_repetir(lista_producao_gramatica,line[count-1])#verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_producao_gramatica.append(line[count-1])      #adiciona as produções da gramaticas

                        tem = nao_repetir(lista_elementos_producao_all,line[count-1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_elementos_producao_all.append(line[count-1])  # enchendo a lista all


                    if letra_gramatica==' ' and (line[count+2]==' ' or line[count+2]=='\n' )and line[count+1]!='|' and line[count+1] != 'ε': # condição para pegar simbolos terminiais e add na lista de produções
                        #print(line[count+1])
                        tem = nao_repetir(lista_producao_gramatica,line[count+1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_producao_gramatica.append(line[count+1])          #

                        tem = nao_repetir(lista_elementos_terminais,line[count+1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_elementos_terminais.append(line[count+1])         #

                        tem = nao_repetir(lista_elementos_producao_all,line[count+1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_elementos_producao_all.append(line[count+1])  # enchendo a lista all


                    count = count + 1
            else:                                                               #se for token entra aqui
                #print('É token')
                count = 0                                                       #condatador para auxiliar na elemento que seraá icluído
                for letra_gramatica in line:                                    #for para andar ccarcter à caracter na linha
                    if letra_gramatica != '\n':                                 # para pegar simbolos não terminais das produções
                        tem = nao_repetir(lista_producao_token,line[count])     #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_producao_token.append(line[count])
                        tem = nao_repetir(lista_elementos_producao_all,line[count])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_elementos_producao_all.append(line[count])    # enchendo a lista all

                    else:                                                       #pegando os simbolos terminais dos tokens
                        tem = nao_repetir(lista_elementos_terminais,line[count-1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_elementos_terminais.append(line[count-1])         #pegando os simbolos que não são terminais

                        tem = nao_repetir(lista_elementos_producao_all,line[count-1])   #verifica se o elemento está na lista ser retornar -1 não tem na lista
                        if tem < 0:
                            lista_elementos_producao_all.append(line[count-1])  # enchendo a lista all
                    count = count + 1
                                                                                #carregar as produções no af
        matriz = criar_matriz(lista_elementos_terminais,lista_nome_gramatica,
                                lista_producao_gramatica,lista_producao_token,
                                lista_elementos_producao_all, alpha_lower,
                                alpha_upper, file)

        file.seek(0,0)
        lista_gramaticas_end = n_gramatica_terminal(file)                       #função para verificar a gramatica é terminal ou não


        file.seek(0,0)
        first_gramatica = 0
        for l_file in file:
            if l_file[0] == '<':                                                #construindo apartir da gramatica
                n_gramatica_letra = l_file[1]                                   #peguei a letra que dá nome à gramatica
                n_linha = localiza_letra_gramatica (matriz,n_gramatica_letra)   # a linha que se encotra a grámatica na matriz
                if first_gramatica == 0:
                    matriz[n_linha][27] = '+'                                   #seta a gramatica como inicial
                first_gramatica = first_gramatica + 1
                ccount = 0
                for c in l_file:                                                #for para descobrir as produções por linha no arquivo
                    if ccount>6 and l_file[ccount-1] ==' ' and l_file[ccount]!='|' and (l_file[ccount+1]=='<'
                        or l_file[ccount+1] == '\n' or l_file[ccount+1]==' '):#condições para ser produção de uma grámatica
                        #print(l_file[ccount])
                        if l_file[ccount] != 'ε':                               #mapea as produções menos a epsilon
                            if l_file[ccount+1] == '\n' or l_file[ccount+1] == ' ':                        #se for uma produção final no final
                                n_linha_vazia = busca_linha_vazia(matriz,lista_nome_gramatica)#função para encontrar uma linha vazia na matriz para incluir o elemento terminal
                                n_coluna = encontra_posicao_da_producao(matriz,l_file[ccount]) # pega a coluna da posição do elemento que será incluso no afnd
                                elemento = matriz[n_linha_vazia][0]
                                elemento = vazio(matriz,elemento,n_linha,n_coluna)# chama função para ver se é vazio se não for vai incluir o elemento se for vai add o que já tem na tabela
                                matriz[n_linha_vazia][28] = '*'                 #Vai setrar a gramatica com terminal
                                matriz[n_linha][n_coluna] = elemento            #inclui o elemento
                            else:                                               #casos normais ok!
                                n_coluna = encontra_posicao_da_producao(matriz,l_file[ccount]) # pega a coluna da posição do elemento que será incluso no afnd
                                elemento = l_file[ccount+2]                     #Pega para qual a gramáticaa vai
                                elemento = vazio(matriz,elemento,n_linha,n_coluna)# chama função para ver se é vazio se não for vai incluir o elemento se for vai add o que já tem na tabela
                                matriz[n_linha][n_coluna] = elemento
                        else:                                                    #tratar as epsilon produções só vou setar a gramatica com final
                            matriz[n_linha][28] = '*'
                    ccount = ccount + 1

            else:                                                               #construindo afnd partir do token
                n_gramatica_token = l_file[0]                                   #peguei a primeira letra do token
                ccount = 0
                for c in l_file:
                    if ccount == 0:                                             #se for a produção inicial do token
                        inicial =  encontra_inicial(matriz)                     #entcontra na matriz o +
                        matriz[inicial][27] = '+'
                        n_coluna = encontra_posicao_da_producao(matriz,l_file[ccount])
                        n_linha_vazia = busca_linha_vazia(matriz,lista_nome_gramatica)
                        elemento = matriz[n_linha_vazia][0]
                        elemento = vazio(matriz,elemento,inicial,n_coluna)
                        print(elemento)
                        matriz[inicial][n_coluna] = elemento                    #inclui o elemento que será o destino da próxima produção meio de sentença

                    else:
                        n_coluna = encontra_posicao_da_producao(matriz,l_file[ccount]) #encontra linha coluna da próxima produção
                        n_linha_vazia = busca_linha_vazia(matriz,lista_nome_gramatica) #encontra próxima linha vazia
                        matriz[n_linha_vazia][n_coluna] = '$'
                        next_n_linha_vazia = busca_linha_vazia(matriz,lista_nome_gramatica) #verifi se essa linha não vai ser usada na grámatica até achar uma linha vazia
                        elemento = matriz[next_n_linha_vazia][0]                       #encontra a próxima gramática para a produção
                        matriz[n_linha_vazia][n_coluna] = elemento
                        if (l_file[ccount+1]) == '\n':                          #quando for a ultima letra vai fazer o seguinte
                            matriz[next_n_linha_vazia][28] = '*'                #setar o que seria a próxima produção com final
                            break                                               # parar o for por que da problema se cuntinuar
                    ccount = ccount + 1

            """Essa parte do código é a parte do AUTOMATO FINITO DETERMINIZADO"""
        exibir_matriz(matriz)
        matriz_AFD = criar_matriz(lista_elementos_terminais,lista_nome_gramatica,
                                        lista_producao_gramatica,lista_producao_token,
                                        lista_elementos_producao_all, alpha_lower,
                                        alpha_upper, file)

        #wait = input("PRESS ENTER TO CONTINUE...")
        #time.sleep(3)                                                         # pause 3 seconds

        lista_prod_AFD = []                                                     #lista para armazenar as produções que são colocadas no afd
        n_linha1_AFD =  encontra_inicial(matriz)                                #Encontrar a primeira produção inicial S
        conta_c = 0
        for i in range (29):
            matriz_AFD[1][conta_c] = matriz [n_linha1_AFD][conta_c]             #Independente qual a gramática ela vai sempre estar na primeira linha
            str = ''.join(matriz[n_linha1_AFD][conta_c])
            if len(str) > 1:
                str = '[' + str +']'
                matriz_AFD[1][conta_c] = str
            conta_c = conta_c + 1
        lista_prod_AFD.append(matriz_AFD[1][0])                                 # inclui o elemento na lista
        print('primeira condição\n')
        oi = 0
        for i in matriz_AFD:
            if oi <2:
                print(i)
            oi = oi + 1
        print('\n')
        wait = input("PRESS ENTER TO CONTINUE...")


        contador_l = 0                                                          #função para busca na matriz afnd a primeira produção disponivel
        contador_c = 0
        contador_colunas = 1
        for l in matriz_AFD:                                                    #vou andar nesse for até o final da outra matriz
            contador_c = 0
            for c in l:
                if contador_l > 0 and contador_c > 0 :                          #para não pegar a primeira linha e a primeira coluna
                    if c != ' ' and c != '+' and c != '*':                      #encontrei as produções na matriz AFD vou continuar o código
                        if contador_colunas < 26:
                            contador_colunas = contador_colunas + 1             # vai me dizer em qual linha vou colcar as produções já tem mais dois pq linha 0                                                                                #e linha 1 já são ocupadas
                        c_string = ''.join(c)                                   #transformo as produções em string
                        conten = nao_repetir(lista_prod_AFD,c)                  #não permite duplicar as produções no afnd
                        if conten<0:
                            lista_prod_AFD.append(c)

                            if len(c_string) > 1:                                   #se o tamanho delas forem maior do que 1 siginifica que tem mais produções
                                j=0                                                 #contador qualquer
                                lista_string = []                                   #lista para reorganizar os elementos
                                for i in c_string:                                  #for para eliminar a virgula
                                    if c_string[j] != ',':
                                        lista_string.append(c_string[j])            # pega os elementos que não são virgula
                                    j = j + 1
                                c_string = ''.join(lista_string)
                                matriz_AFD[contador_colunas][0] = c_string          #guarda a nova produção para colocar no afnd
                                controle = 0
                                lista_aux = []
                                for i in range(len(c_string)):                      #add elementos das novas produções
                                    if c_string[i] != '[' and c_string[i] != ']':
                                        qual_linha = localiza_letra_gramatica(matriz,c_string[i]) #pega a posição que será copiada
                    #A PARTE QUE EU MAIS SOFRI NO DESENVOLVIMENTO
                                        aux = 0                                     #Váriaveis auxiliares
                                        s_aux2=''                                   #string auxiliares
                                        for x in matriz:
                                            if aux == qual_linha:
                                                if controle == 0:
                                                    string_aux1 = x
                                                else:
                                                    string_aux2 = x
                                                    for ii in range(29):
                                                        s_aux = string_aux2[ii] + string_aux1[ii]
                                                        if s_aux == '  ':                           #se tiver 2 espaços par ter somente 1
                                                            s_aux = ' '
                                                        elif s_aux == '**' or s_aux == ' *' or s_aux == '* ':   #tirar os espaços e ou um  *
                                                            s_aux = '*'
                                                        else:                       # condição eliminar espaço das produções e colocar entre []
                                                            s_aux2=''
                                                            for u in range (len(s_aux)):
                                                                if(s_aux[u]) != ' ':
                                                                    s_aux2 = s_aux2 + s_aux[u]
                                                            if len(s_aux2) > 1:                 # esse if senão ia ter um um elemento com ''[x]''
                                                                s_aux = '['+s_aux2+']'
                                                            else:
                                                                s_aux = s_aux2

                                                        lista_aux.append(s_aux)

                                                #print(lista_aux)
                                                controle = controle + 1
                                            aux = aux + 1
                                print('segunda condição\n')
                                print(lista_aux)
                                for k in range (29):
                                    matriz_AFD[contador_colunas][k] = lista_aux[k]
                                wait = input("PRESS ENTER TO CONTINUE...")

                            else:                                                   # se for só uma produção
                                c_string = c
                                matriz_AFD[contador_colunas][0] = c                 #guarda a nova produção para colocar no afnd
                                qual_linha = localiza_letra_gramatica(matriz,c)     #entcontrar as produções em da letra
                                for i in range(29):                                 #for para copiar as produções para AFD
                                    str = ''.join(matriz[qual_linha][i])
                                    if len(str) > 1:                                #se for mais de um caractere vai colocar []
                                        str = '[' + str +']'
                                        matriz_AFD[contador_colunas][i] = str       #incluí o elemento na Matriz AFD
                                    else:
                                        matriz_AFD[contador_colunas][i]= matriz[qual_linha][i] #incluí o elemento na Matriz AFD

                                print('terceira condição')
                                oi =0
                                for i in matriz_AFD:
                                    if contador_colunas == oi:
                                        print(i)
                                    oi = oi + 1
                                print('\n')
                                wait = input("PRESS ENTER TO CONTINUE...")
                        else:
                             contador_colunas = contador_colunas - 1
                contador_c = contador_c + 1
            contador_l = contador_l + 1





        print(lista_prod_AFD)
        print("------------------------------------------------------------MATRIZ - AFD--------------------------------------------------------------------------------")
        exibir_matriz(matriz_AFD)

    finally:                                                                    #Vai executar mesmo com erros acima
        file.close()                                                            #Fechando o arquivo



def existe():                                                                   #Verifica se o arquivo entrada.txt existe
    if os.path.isfile('entrada.txt'):
        print('Arquivo de entrada OK!!! \n')
    else:
        print('Não existe arquivo de entrada')                                  #
        sys.exit(0)



"""def afnd_gramatica(file):                                                    #função para ler a gramática
    matriz_afnd = criar_matriz()
    exibir_matriz(matriz_afnd)
    print("É gramática")
    file.seek(0,0)
    return 0

def afnd_token():                                                               #função para token
    print("É token")
    matriz_afnd = criar_matriz()
    exibir_matriz(matriz_afnd)
    return 0"""

def criar_matriz(lista_elementos_terminais,lista_nome_gramatica,
                lista_producao_gramatica,lista_producao_token,
                lista_elementos_producao_all, alpha_lower,
                alpha_upper,file):                                                   #função para criar matriz
    file.seek(0,0)
    m = 27                                                                      #quantidade de listas dentro de uma lista
    n = 29                                                                      #coluna quantidade de itens dentro de uma lista
    n_gramatica = 0
    n_producao = 0
    tag = 0
    tag2 = 0
    #lista_producao = lista_producao_token + lista_producao_gramatica
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            if (j == 0) and (i == 0):                                           #defini a posição 0 0 da matriz
                elemento = 'Ø'
                linha.append((elemento))
            elif (j >= 1) and (i==0) :                                          #defini os elementos de produção
            #vou trabalhar com a lista de ista_producao_gramatica e lista_producao_token
                """tamanho = len(lista_elementos_producao_all)                  # essa parte do código incluiria somente as produções existentes
                if n_producao < tamanho:
                    elemento = lista_elementos_producao_all[n_producao]
                    n_producao = n_producao + 1
                else:
                    elemento = 96 + j"""
                tamanho = len(alpha_lower)                                      #essa parte inclui afabeto minusculo com possivesi produções
                if n_producao < tamanho:
                    elemento = alpha_lower[n_producao]
                    n_producao = n_producao + 1
                else:
                    #elemento = 96 + j
                    if 96 + j == 123:
                        elemento = 'IN'
                    if 96 + j == 124:
                        elemento = 'END'

                linha.append((elemento))

            elif (j>0) and (i>0):                                               #gera o afnd
                elemento = ' '
                linha.append((elemento))
            else:                                                                #deifni os Elementos que dão nome as regras
                #vou trabalhar com a lista de lista_nome_gramatica
                """tamanho = len(lista_nome_gramatica)                          # essa parte só add os nomes de grámaticas já existentes
                if n_gramatica < tamanho:
                    #elemento=lista_nome_gramatica[n_gramatica]
                    elemento=lista_nome_gramatica[n_gramatica]
                    n_gramatica= n_gramatica + 1
                else:
                    elemento = i + 64"""
                tamanho = len(alpha_upper)                                      #esse código coloca as letra MAUIUSCULAS para compor os nomes das gramaticas
                if n_gramatica < tamanho:
                    #elemento=lista_nome_gramatica[n_gramatica]
                    elemento=alpha_upper[n_gramatica]
                    if tag == 0:                                                #Condição para deixar o S como produção inicial
                        elemento = 'S'
                        tag = 1
                        n_gramatica= n_gramatica - 1
                    if  elemento == 'R':                                        #condição para não repetir o 'S'
                        n_gramatica= n_gramatica + 1
                    n_gramatica= n_gramatica + 1
                else:
                    elemento = i + 64

                linha.append((elemento))
        matriz.append(linha)
    return matriz


def exibir_matriz(matriz):                                                      #função para exibir matriz
    """Exibe uma matriz na saída padrão"""
    for linha in matriz:
        for c in linha:
            space = 5 - len(c)
            for i in range(space):
                print(' ',end='')
            print(" {} |".format(c), end='')
            
        print()
        #string = ''.join(linha)
        #file = open('saida.txt','a+')
        #file.write(string)
        #file.write('\n')
        #print(linha)
    #file.close()

def nao_repetir(lista_x,char_x):                                                #Função para Verificar a existencia de um elemento na lista
    #print(lista_x, char_x)
    string = ''.join(lista_x)                                                   #transformo a lista em um strig
    existe = string.find(char_x)                                                #uso uma função para ver se caractere tem na string
    return existe                                                               #se não tem retorna -1

def n_gramatica_terminal(file):                                                 #verica as regras que são terminais
    file.seek(0,0)                                                              #posiciona no começo do arquivo
    lista_gramaticas_end= []                                                    #lista para armazenar os elementos
    for l in file:                                                              #for para andar na linha do arquivo
        count = 0                                                               #para referencia
        for w in l:                                                             #para andar na linha
            if w ==' ' and (l[count+2]==' ' or l[count+2]=='\n' )and l[count+1]!='|': #condição para reconhecer elementos terminais
                tem = nao_repetir(lista_gramaticas_end,l[1])                    #função para não repetir os elementos treminais na lista
                if tem < 0:                                                     #retorno da função indica se tem ou não na lista
                    lista_gramaticas_end.append(l[1])                           #inclui na lista dos terminais
                    break                                                       #para o for
            count = count + 1                                                   #referencia
    return lista_gramaticas_end                                                 #retorna a lista produzida

def localiza_letra_gramatica (matriz,x):                                        #encontra em qual linha dever ser incluido o elemento
    count = 0
    for qual_linha in matriz:
        if qual_linha[0] == x:
            return count
        count = count + 1

def encontra_posicao_da_producao (matriz,x):                                    #encontra em qual posição da coluna vai ser incluido o elemento
    count = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == x:
                return count
            count = count + 1

def vazio(matriz,elemento,x,y):                                                 #essa função retorna uma string se tiver um elemento já na matriz
    if matriz[x][y] == ' ':
        return elemento
    else:
        s = matriz[x][y]
        if s.count(elemento) == 0:
            s = s+','+elemento
            return s
        else:
            return s


def busca_linha_vazia(matriz,lista_nome_gramatica):                             # função que retorna a posição de uma lista vazia
    count_l = 0                                                                 #contador de linhas
    string = ''.join(lista_nome_gramatica)                                      # transformo a lista em uma string
    for l in matriz:                                                            #for para andar nas linhas
        count_c = 0                                                             #contador para colunas
        for c in l:                                                             #for em colunas
            if count_c > 0:                                                     #primeira coluna não pode entrar na regra
                if matriz [count_l][count_c] !=' ':                             #se encontrar algun espaço diferente de fazio
                    break                                                       #vai para a próxima linha
                if count_c == 27:                                               #se contador for 27
                    end = matriz [count_l][28]
                    s = string.find(matriz [count_l][0])                        #s recebe se existe ou não o elemento na lista de nos de produções
                    if  s < 0 and end != '*' :                                  #se s não tiver vai retornar -1
                        return count_l                                          #retorna a posição da linha
            count_c = count_c + 1
        count_l = count_l + 1

def encontra_inicial(matriz):                                                   #Função que retorna a posição inicial
        count_l = 0
        for l in matriz:
            if matriz[count_l][27] == '+':
                inicial = matriz[count_l][27]
                return count_l
            count_l = count_l + 1
            if (count_l) >= 27:
                return 1
        #print(count_l)


if __name__ == "__main__":
    main()
