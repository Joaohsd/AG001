'''
Nome:       João Henrique Silva Delfino
Matrícula:  1662
Curso:      GEC


Exercício 2 - Derivada e Integral para determinação da velocidade e aceleração

'''

#Importando as funções da biblioteca sympy
from sympy import Derivative, Integral, Symbol, cos, pi

#Constante
c = 1662%10

#Definição da função a qual define a velocidade instantânea
def velocidade(t):
    #Amplitude do movimento é de 5 cm
    a = 5.0
    #Frequência do movimento é de 5 Hz
    f = 5.0
    #Velocidade angular do movimento é definida por 2*pi*f
    w = 2*pi*f
    return a*w*cos(w*t - c)

#Define t como uma variável
t = Symbol('t')

#Cálculo e exibição da equação do deslocamento, em que o deslocamento é a integral da velocidade
equacao_deslocamento = Integral(velocidade(t), t).doit()
print('Equação do deslocamento: ')
print(equacao_deslocamento, " [cm]", "\n")

#Cálculo e exibição da equação da acelaração, em que a aceleração é a derivada da velocidade
equacao_aceleracao = Derivative(velocidade(t), t).doit()
print('Equação da aceleração: ')
print(equacao_aceleracao, " [cm/s^2]", "\n")

#Cálculo e exibição do valor da aceleração em t = 4 segundos
aceleracao_em_4_seg = Derivative(velocidade(t), t).doit().subs({t:4})
print('Aceleração para t = 4 segundos: ')
print(round(float(aceleracao_em_4_seg),3), " [cm/s^2]", "\n")