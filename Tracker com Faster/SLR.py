import cv2

#Velocidade ---------------------------------------------
razao = 2
#--------------------------------------------------------

#Direções -----------------------------------------------
cima = 0
direita = 1
baixo = 2
esquerda = 3
#--------------------------------------------------------

#Propriedades do primeiro retângulo - R0  ---------------
altura_ret_0 = 200 #altura do retângulo 0
largura_ret_0 = 300 #largura do retângulo 0
#--------------------------------------------------------

#Cores BGR ----------------------------------------------
roxo = (65, 9, 88)
laranja = (0, 165, 255)
#--------------------------------------------------------


def criaRet(altura, largura, cor, frame_process, vel):  #Cria um retângulo de altura, largura, cor e velocidade 
                                                        #conforme os parâmetros recebidos

    #Frame process é o frame em que será inscrito o retângulo
    
    yC = frame_process.shape[0] / 2 #Coordenada Y do centro
    xC = frame_process.shape[1] / 2 #Coordenada X do centro

    cima = int (yC - altura/2) #Lado de cima do retângulo
    baixo = int (yC + altura/2) #Lado de baixo do retângulo
    esquerda = int(xC - largura/2) #Lado esquerdo do retângulo
    direita = int(xC + largura/2) #Lado direito do retângulo

    p0 = (esquerda, cima) #Ponto p0 do retângulo
    p1 = (direita, baixo) #Ponto p1 do retângulo

    pL = [cima*(-1), direita, baixo, esquerda*(-1)] #Ponto p0 do retângulo em formato de lista

    cv2.rectangle(frame_process, p0, p1, cor, 1) #Escreve o retângulo

    ret = [pL, vel] #Cria vetor Retângulo que contem os pontos formadores e a velocidade

    return ret


def criaListaRetangulos(ret0, numero_de_retangulos, frame_process): #Cria a lista de todos os retângulos a partir do centro

    yC = frame_process.shape[0] / 2 #Coordenada Y do centro
    xC = frame_process.shape[1] / 2 #Coordenada X do centro

    #Divide a quantidade que será iterada a altura e largura. Também inicia a menor velocidade.
    altura_por_retangulo = (yC - altura_ret_0/2) / numero_de_retangulos
    largura_por_retangulo = (xC - largura_ret_0/2) / numero_de_retangulos
    menor_velocidade = 1

    #Inicia uma lista vazia
    lista_retangulos = []

    altura = altura_ret_0 + altura_por_retangulo*2
    largura = largura_ret_0 + largura_por_retangulo*2

    lista_retangulos.append(ret0)

    #Loop para formar a lista
    for i in range(numero_de_retangulos):

        #print(i)
        vel = menor_velocidade*(i+2) #Velocidade do retângulo
        retangulo = criaRet(altura, largura, laranja, frame_process, vel) #Criando cada retângulo da lista
        altura += altura_por_retangulo*2 #altura do retângulo i da lista
        largura += largura_por_retangulo*2 #largura do retângulo i da lista
        lista_retangulos.append(retangulo) 

    return lista_retangulos

def conditions(coordenatesTarget, listRectangles): #Verifica se a target passou em cada diração e retângulo
    target = [coordenatesTarget[i]*(-1) if i%3==0 else coordenatesTarget[i] for i in range(4)]
    positions = {0: 'top', 1: 'right', 2: 'bottom', 3: 'left'}
    limit_Numbers = len(listRectangles)

    for direction in range(4): #Verifica em cada direção
        for rectangle in range(limit_Numbers-1): #Verifica em cada retângulo
            if listRectangles[rectangle][0][direction] <= target[direction] and listRectangles[rectangle+1][0][direction] > target[direction]:
                print('r{}: {}'.format(rectangle, positions.get(direction)))
                return rectangle
                break
            elif listRectangles[limit_Numbers-1][0][direction] == target[direction]:
                print('r{}: {}'.format(limit_Numbers - 2, positions.get(direction)))
                return limit_Numbers - 2

def if_antigo(direcao, lista_ret, top, right, bottom, left):

    if direcao == esquerda:
        if lista_ret[0][0][0] >= left:
            t1=razao
        else:
            t1=0

        if lista_ret[1][0][0] >= left:
            t2=razao
        else:
            t2=0
        
        if lista_ret[2][0][0] >= left:  
            t3=razao
        else:
            t3=0
        
        if lista_ret[3][0][0] >= left:  
            t4=razao
        else:
            t4=0

        return (t1 + t2 + t3 + t4)

    elif direcao == cima:
        if lista_ret[0][0][1] >= top:
            t1=razao
        else:
            t1=0

        if lista_ret[1][0][1] >= top:
            t2=razao
        else:
            t2=0
        
        if lista_ret[2][0][1] >= top:  
            t3=razao
        else:
            t3=0
        
        if lista_ret[3][0][1] >= top:  
            t4=razao
        else:
            t4=0

        return (t1 + t2 + t3 + t4)

    elif direcao == direita:
        if lista_ret[0][1][0] <= right:
            t1=razao
        else:
            t1=0

        if lista_ret[1][1][0] <= right:
            t2=razao
        else:
            t2=0
        
        if lista_ret[2][1][0] <= right:  
            t3=razao
        else:
            t3=0
        
        if lista_ret[3][1][0] <= right:  
            t4=razao
        else:
            t4=0

        return (t1 + t2 + t3 + t4)

    elif direcao == baixo:
        if lista_ret[0][1][1] <= bottom:
            t1=razao
        else:
            t1=0

        if lista_ret[1][1][1] <= bottom:
            t2=razao
        else:
            t2=0
        
        if lista_ret[2][1][1] <= bottom:  
            t3=razao
        else:
            t3=0
        
        if lista_ret[3][1][1] <= bottom:  
            t4=razao
        else:
            t4=0
        
        return (t1 + t2 + t3 + t4)