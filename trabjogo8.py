#Rafael Victor Marciano Arriel 201811050
#Renan Fernandes Guimaraes 201711917

import copy
from copy import deepcopy
import numpy as np
import time
import timeit
#from numpy.lib.function_base import append


#FUNÇOES 
##############################################################################

#Descobre qual algoritimo é mais rapido/ eficiente
def maisR(tabIn,tabinlis,tabR):
  
  tempo = False
  
  i=timeit.default_timer()
  buscaA(tabinlis, tabR,tempo)
  j=timeit.default_timer()
  x = (j-i)
  
  i=timeit.default_timer()
  buscaBFS(tabIn)
  j=timeit.default_timer()
  y = (j-i)
  

  if x>y:
    print('A busca A* teve um tempo de execução de: ',x,'s')
    print('Portanto a busca cega foi mais rapida, com um tempo de execução de: ',y,'s')
  else:
    print('A Busca BFS teve um tempo de execução de:',y,'s')
    print('Portanto a busca A* foi mais rapida, com um tempo de execução de: ',x,'s')


#Funçoes para A*
##############################################################################

#Chama a busca A* calcula tempo de execução printa resultados
def buscaA(tabinlis, tabR, tempo):
  
  x=timeit.default_timer()
  state, visited = buscaAs(tabinlis, tabR) 
  y=timeit.default_timer()
  tEx = (y-x)
  bestsol = bestSol(state)
  print('As jogadas foram:\n')
  print(str(bestsol).replace('[', ' ').replace(']', ''),'\n')
  totalmoves = len(bestsol) - 1
  print('Total de Jogadas: ',totalmoves,'\n')
  visit = len(state) - visited
  print('Total de nós visitados: ',visit, "\n")
  print('Total gerado: ', len(state),'\n')
  if tempo == True:
    print('Tempo de execução:',tEx,'s')

#pega a entrada dos estados atuais e avalia o melhor caminho para o estado resolvido
def bestSol(state):
    bestsol = np.array([], int).reshape(-1, 9)
    count = len(state) - 1
    while count != -1:
        bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
        count = (state[count]['parent'])
    return bestsol.reshape(-1, 3, 3)
   
#verifica a exclusividade do estado de iteração (it), se ele foi percorrido anteriormente ou não.
def all(checkarray):
    set=[]
    for it in set:
        for checkarray in it:
            return 1
        else:
            return 0

#calcula o número de peças perdidas no estado atual em comparação com o estado resolvido
#def pecaPerdida(puzzle,goal):
    #mscost = np.sum(puzzle != goal) - 1
    #return mscost if mscost > 0 else 0

#identifica as coordenadas de cada um dos valores de resolvido ou estado inicial
def coordinates(puzzle):
    pos = np.array(range(9))
    for p, q in enumerate(puzzle):
        pos[q] = p
    return pos


#funçoes para BFS
##############################################################################

#chama a busca bfs calcula tempo de execução
def buscaCega(tabIn):
  x=timeit.default_timer()
  buscaBFS(tabIn)
  y=timeit.default_timer()
  tEx = (y-x)
  print('Tempo de execução:',tEx,'s')
  
#Verifica se ganhou
def verificaGanhou(tab): 
  a = True
  if tab[0][0]!=0: a = False
  if tab[0][1]!=1: a = False
  if tab[0][2]!=2: a = False
  if tab[1][0]!=3: a = False
  if tab[1][1]!=4: a = False
  if tab[1][2]!=5: a = False
  if tab[2][0]!=6: a = False
  if tab[2][1]!=7: a = False
  if tab[2][2]!=8: a = False
  return a

#Verifica se os dois tabuleiros são iguais
def tabuleirosIguais(tab1, tab2): 
  sao_iguais = True 
  for i in range(3):
    for j in range(3):
      if tab1[i][j] != tab2[i][j]:
        sao_iguais = False
  return sao_iguais

#Imprime o tabuleiro 
def imprimeTab(tab): 
  print(tab[0])
  print(tab[1])
  print(tab[2])
  print('\n')
  
#retorna um conjunto de nós filhos com as próximas jogadas possíveis
def expandir(tab): 
  
  #armazena os tabuleiros jogadas possíveis
  jogadas = [] 
  
  #se vazio esta no meio do tabuleiro
  if tab[1][1]==0: 
    #move pra baixo
    a = copy.deepcopy(tab) #copia objeto
    a[1][1] = a[0][1]
    a[0][1] = 0
    a[3][0] = a[3][0]+1 #profundidade nó
    a[3][1] = tab #cria referencia p/ nó pai
    jogadas.append(a)
    
    #move pra direita
    a = copy.deepcopy(tab) #copia objeto
    a[1][1] = a[1][0]
    a[1][0] = 0
    a[3][0] = a[3][0]+1 #profundidade nó     
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra esquerda
    a = copy.deepcopy(tab) #copia objeto
    a[1][1] = a[1][2]
    a[1][2] = 0
    a[3][0] = a[3][0]+1 #profundidade nó   
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra cima
    a = copy.deepcopy(tab) #copia objeto
    a[1][1] = a[2][1]
    a[2][1] = 0
    a[3][0] = a[3][0]+1 #profundidade nó     
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no canto esquerdo superior
  elif tab[0][0]==0:
    
    #move pra cima
    a = copy.deepcopy(tab) 
    a[0][0] = a[1][0]
    a[1][0] = 0
    a[3][0] = a[3][0]+1     
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra esquerda
    a = copy.deepcopy(tab) 
    a[0][0] = a[0][1]
    a[0][1] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no canto direito superior
  elif tab[0][2]==0:
    #move pra cima
    a = copy.deepcopy(tab) 
    a[0][2] = a[1][2]
    a[1][2] = 0
    a[3][0] = a[3][0]+1     
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra direita
    a = copy.deepcopy(tab) 
    a[0][2] = a[0][1]
    a[0][1] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no canto inferior esquerdo
  elif tab[2][0]==0:
    #move pra baixo
    a = copy.deepcopy(tab) 
    a[2][0] = a[1][0]
    a[1][0] = 0
    a[3][0] = a[3][0]+1      
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra esquerda
    a = copy.deepcopy(tab) 
    a[2][0] = a[2][1]
    a[2][1] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no canto inferior direito
  elif tab[2][2]==0:
    #move pra baixo
    a = copy.deepcopy(tab) 
    a[2][2] = a[1][2]
    a[1][2] = 0
    a[3][0] = a[3][0]+1     
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra direita
    a = copy.deepcopy(tab) 
    a[2][2] = a[2][1]
    a[2][1] = 0
    a[3][0] = a[3][0]+1   
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no meio da linha de cima
  elif tab[0][1]==0:
    #move pra cima
    a = copy.deepcopy(tab) 
    a[0][1] = a[1][1]
    a[1][1] = 0
    a[3][0] = a[3][0]+1     
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra direita
    a = copy.deepcopy(tab) 
    a[0][1] = a[0][0]
    a[0][0] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
   
    #move pra esquerda
    a = copy.deepcopy(tab) 
    a[0][1] = a[0][2]
    a[0][2] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no meio da linha de baixo
  elif tab[2][1]==0:
    #move pra baixo
    a = copy.deepcopy(tab) 
    a[2][1] = a[1][1]
    a[1][1] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra direita
    a = copy.deepcopy(tab) 
    a[2][1] = a[2][0]
    a[2][0] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra esquerda
    a = copy.deepcopy(tab) 
    a[2][1] = a[2][2]
    a[2][2] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no meio da coluna da esquerda
  elif tab[1][0]==0:
    #move pra baixo
    a = copy.deepcopy(tab) 
    a[1][0] = a[0][0]
    a[0][0] = 0
    a[3][0] = a[3][0]+1      
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra cima
    a = copy.deepcopy(tab) 
    a[1][0] = a[2][0]
    a[2][0] = 0
    a[3][0] = a[3][0]+1     
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra esquerda
    a = copy.deepcopy(tab) 
    a[1][0] = a[1][1]
    a[1][1] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
  
  #se vazio esta no meio da coluna da direita
  elif tab[1][2]==0:
    #move pra baixo
    a = copy.deepcopy(tab) 
    a[1][2] = a[0][2]
    a[0][2] = 0
    a[3][0] = a[3][0]+1    
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra cima
    a = copy.deepcopy(tab) 
    a[1][2] = a[2][2]
    a[2][2] = 0
    a[3][0] = a[3][0]+1   
    a[3][1] = tab
    jogadas.append(a)
    
    #move pra direita
    a = copy.deepcopy(tab) 
    a[1][2] = a[1][1]
    a[1][1] = 0
    a[3][0] = a[3][0]+1     
    a[3][1] = tab
    jogadas.append(a)

  #retorna o conjunto de jogadas/ nós
  return jogadas      

#imprime as as jogadas  
def imprimejogadas(tab):
  print("As jogadas foram:\n")
  pilha = []
  total = tab[3][0]
  
  while(tab[3][1] != None): #vai até o nó raiz
    pilha.append(tab)
    tab = tab[3][1]
  pilha.append(tab)
  while(len(pilha)>0):
    temp = pilha.pop()
    imprimeTab(temp)
  print("Total de jogadas:",total)


#HEURÍSTICA
##############################################################################

#calcula o custo da distância de Manhattan entre cada dígito do quebra-cabeça (estado inicial e o estado resolvido)
def manhattan(puzzle, goal):
    a = abs(puzzle // 3 - goal // 3)
    b = abs(puzzle % 3 - goal % 3)
    mhcost = a + b
    return sum(mhcost[1:])



#ALGORITMOS DE BUSCA
##############################################################################

#busca A*
def buscaAs(puzzle, goal):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])

    dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
    
    #inicializan o pai gn e hn onde hn é chamada de função de manhattan
    costg = coordinates(goal)
    parent = -1
    gn = 0
    hn = manhattan(coordinates(puzzle), costg)
    state = np.array([(puzzle, parent, gn, hn)], dtstate)

    #Faze uso de filas prioritárias com posição como chaves e fn como valor.
    dtpriority = [('position', int),('fn', int)]
    priority = np.array( [(0, hn)], dtpriority)
    
    cont = 0
    
    while 1:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])     
        position, fn = priority[0]                                                 
        priority = np.delete(priority, 0, 0)  
        #classifica fila de prioridade usando mesclagem de classificação o primeiro elemento é escolhido para explorar remover da fila o que estamos explorando
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
        #Identifique o espaço vazio na entrada
        blank = int(np.where(puzzle == 0)[0])       
        gn = gn + 1                              
        c = 1
        start_time = time.time()
        
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                #gera novo estado como cópia do atual
                openstates = deepcopy(puzzle)                   
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]             
                
                # A função all é chamada, se o nó foi previamente explorado ou não
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():    
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" Este tabuleiro não tem solução!!! \n")
                        exit 
                    
                    #chama função manhattan para calcular o custo
                    hn = manhattan(coordinates(openstates), costg)    
                    
                    #gera e adicionar novo estado na lista
                    q = np.array([(openstates, position, gn, hn)], dtstate)         
                    state = np.append(state, q, 0)
                    
                    #f(n) é a soma do custo para alcançar o nó e o custo para mudar do nó para o estado resolvido
                    fn = gn + hn                                        
                    q = np.array([(len(state) - 1, fn)], dtpriority)    
                    priority = np.append(priority, q, 0)
                      
                    #Verificar se o nó em estados abertos está correspondendo ao estado resolvido.
                    if np.array_equal(openstates, goal):                              
                        print(' *** Solução encontrada!!!*** \n')
                        return state, len(priority)
            
        cont+=1
        print('Solucionando o problema espere um momento, isso pode levar algum tempo ',cont)
        
                        
    return state, len(priority)


#Busca BFS (sem nós repetidos)
def buscaBFS(tab_inicial):
  fila = []
  filaRepet = [] #usada para verificar expanção de repetidos
  fila.append(tab_inicial) # adiciona no fim da fila
  filaRepet.append(tab_inicial)
  nosExp = 0 # numero de nós expandidos
  while(len(fila)>0):
    nodoTemp = fila.pop(0) # retira do início da fila
    nosExp += 1
    #print('Nó expandido:', nos_exp,'\n')
    print('Solucionando o problema espere um momento, isso pode levar algum tempo ',nosExp)
    #imprimeTab(nodoTemp)
    
    if verificaGanhou(nodoTemp) == True:
      print("*** Solução encontrada!!!*** \n")
      imprimejogadas(nodoTemp)
      break;
    else:
      nodosFilhos = expandir(nodoTemp)
      for nt in nodosFilhos:
        #verifica se nós já foi expandido
        #percorre toda a filaRepet e ver se já existe
        jaExiste = False
        for x in filaRepet:
          if(tabuleirosIguais(nt,x)):
            jaExiste = True
            break # se já achou repetido para a busca
        if(jaExiste==False):
          fila.append(nt)
          filaRepet.append(nt)



#MENU | MAIN
##############################################################################

tabIn = []
tabinlis = []
tabR = [0,1,2,3,4,5,6,7,8]

print('*********JOGO DOS 8 COM INTELIGENCIA ARTIFICIAL*********')
print('Digite as peças do tabuleiro 0-8')
print('Não digite peças(numeros) Repitidos')
print('Digite linha por linha do tabuleiro')
#print('Digite numero por numero do tabuleiro, serão dividos depois 3 para cada linha')
print('0 = espaço vago no tabuleiro')


#input 1 por 1
#for i in range(9):
 # tab_inicialn.append(int(input(">>")))

#input linha por linha numero separado por espaço
cont = 0
for i in range(3):
  print("Linha",i+1,"digite 3 numeros separdos por espaço")
  x=input(">>")
  y=x.split(sep=" ")
  
  for j in range(3):
    tabinlis.append(int(y[j]))
  
  y.clear
  cont+=3

#transposição de uma lista pra outra 
cont = 0
for i in range (3):
    x = []
    for j in range(3):
        x.append(tabinlis[j+cont])
    
    tabIn.insert(i,x)
    x.clear
    cont+=3

tabIn.append([0,None])

print('O tabuleiro ficou assim!!!')
imprimeTab(tabIn)

print('Informe qual algoritmo deseja utilizar: ')
print("Digite 1: Busca A*")
print("Digite 2: Busca Cega BFS")
print('Digite 3: Se deseja executar os dois e descobrir qual é mais rápido/ eficiente')

op = int(input('>>'))
if(op==1):
  if(tabinlis==tabR):
    print('Este tabuleiro já esta resolvido!!!')
  else:
    tempo = True
    buscaA(tabinlis, tabR,tempo)
   
elif(op==2):
  if(tabinlis==tabR):
    print('Este tabuleiro já esta resolvido!!!')
  else:
    buscaCega(tabIn)

elif(op==3):
  if(tabinlis==tabR):
    print('Este tabuleiro já esta resolvido!!!')
  else:
    maisR(tabIn,tabinlis,tabR)


