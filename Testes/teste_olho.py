###Código atualmente pega apenas UM ponto, assim demonstrando apenas o esqueleto
###da ideia. O ideal seria achar o centro da imagem e a partir dai refletir nos
###2 quadrantes opostos para formar o retângulo com centro no meio.


#Lê a imagem em binário para garantir que as shape 0 e shape 1 sejam height e width
import cv2
video = cv2.VideoCapture(0)
ret, cap = video

dimensions = cap.shape

#Confere quantos pixeis de altura e largura o objeto possui
height = dimensions[0] / 2
width = dimensions[1] / 2

print("\n altura x:     ", width, "\n largura y:    ", height,"\n")

#Pede ao usuário um número arbitrário de retângulos
numero_de_retangulos = int(input("digite aqui o número de retângulos: "))

#Divide a quantidade que será iterada a altura e largura. Também inicia a menor velocidade.
altura_por_retangulo = height / numero_de_retangulos
largura_por_retangulo = width / numero_de_retangulos
menor_velocidade = 1

#Inicia uma lista vazia
lista_retangulos = []


iteracao = 0
#Loop para formar a lista
for i in range(numero_de_retangulos+1):

    #Altura e largura da respectiva iteração. A cada Loop muda a posição
    altura_retangulo = height - (altura_por_retangulo * numero_de_retangulos)
    largura_retangulo = width - (largura_por_retangulo * numero_de_retangulos)

    #Aumenta a velocidade, deve ser futuramente testada em relação ao último retângulo para conferir aonde o target
    #está realmente contido
    velocidade = menor_velocidade*iteracao

    #Adiciona as propriedades dessa iteração a lista
    novo_retangulo = [largura_retangulo, altura_retangulo, velocidade]
    lista_retangulos.append(novo_retangulo)

    numero_de_retangulos -= 1
    iteracao += 1

#Printa a lista formada, cada index é as propriedades daquele retângulo e deve ser acessado como lista_retangulos[n]
print(lista_retangulos)

while(True):
    ret, cap = video.read()
    cv2.imshow('imagenzinha', cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Forcefully Closed")
        cv2.destroyAllWindows()
