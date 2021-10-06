#Importando biblioteca Vpython
from vpython import *
#Importando biblioteca de tempo
import time
#Criando esfera no canto da tela
bola = sphere(pos=vector(-250,6,0), radius=6, color=color.blue)
#Pegando o vetor inicial da bola para utlizar nas formulas de MRU
bolaInicial = vector(-250,6,0)
#Criando o solo mo centro com expessura de 0.5px , largura de 3px e comprimento de 500px
solo = box(pos=vector(0,0,0), size=vector(500,0.5,3), color= color.red)
#Criando os dois letreiros de tempo e velocidade
letreiroTempo = label(pos=vector(20,100,0),color= color.white, text= "Tempo: ")
letreiroVelocidade = label(pos=vector(20,70,0),color= color.white, text= "Velocidade: ")
letreiroNome = label(pos=vector(20,140,0),color= color.white, text= "Mickael Osvaldo de Oliveira")

#Definindo o tempo
Tempo = 0
#Defnindo a velocidade e a aceleração em forma de vetor e em forma de variável
velocidade = 0
aceleracao = 2
bola.vel = vector(0,0,0)
bola.acel = vector(aceleracao,0,0)

#Obtendo o tempo de inicio da execução do código
TempoInicial = time.time()

#Iniciando o laço infinito para que o programa não pause após a primeira execução
while True:
    #Declarando os quadros por segundo de atualização
    rate(60)
    #Subtraindo tempo atual pelo tempo de inicio para obter o tempo total de execução
    Tempo = time.time() - TempoInicial
    #Equações do MRUV S = s0 + vt e V = v0 +at
    bola.vel = (bola.acel * Tempo)
    bola.pos = bolaInicial + (bola.vel * Tempo)
    velocidade = (aceleracao * Tempo)
    #Plotando os letreiro de tempo e velocidade na tela
    letreiroTempo.text = f"Tempo: {Tempo:.2f}s"
    letreiroVelocidade.text = f"Velocidade: {velocidade:.2f}px/s"