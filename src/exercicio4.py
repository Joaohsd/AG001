'''
Nome:       João Henrique Silva Delfino
Matrícula:  1662
Curso:      GEC


Exercício 4 - Solução de sistemas de equações lineares para determinar valores
              das correntes
'''

#Importando as funções da biblioteca sympy
from sympy import Symbol, solve

#Constante
c = 1662%10

def malha_1(i_A, i_B):
    return -20000*i_A - 5000*i_B + 3*(c+1)

def malha_2(i_A, i_B):
    return 5000*i_A + 15000*i_B - 4*(c+1)

#Define i_A e i_B como variáveis
i_A = Symbol('i_A')
i_B = Symbol('i_B')

#Resolvendo o sistema de equaçõs
primeira_malha = malha_1(i_A, i_B)
segunda_malha = malha_2(i_A, i_B)
correntes = solve((primeira_malha,segunda_malha))

#Exibindo os valores das correntes do circuito
print("Correntes:\n")
print("Corrente 1: ", correntes[i_A], "[A]", "\n")
print("Corrente 2: ", correntes[i_B], "[A]", "\n")
print("Corrente 3: ", correntes[i_A] + correntes[i_B], "[A]","\n")
