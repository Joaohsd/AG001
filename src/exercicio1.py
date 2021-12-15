'''
Nome:       João Henrique Silva Delfino
Matrícula:  1662
Curso:      GEC


Exercício 1 - Cálculo de limites

'''

#Importando as funções da biblioteca sympy
from sympy import Limit, Symbol, S

#Constante
c = 1662%10

#Definição da função a qual será calculada o limite
def funcao(x):
    return ((c + 1) - (x ** (1.0/2.0)))/(((c + 1) ** (2.0)) - x)

#Define x como uma variável                                         
x = Symbol('x')

#Cálculo do primeiro limite 
limite = Limit(funcao(x), x, (c + 1)).doit()
print('Limite da função para x tendendo a c+1: ')
print(limite, "\n")

#Cálculo do segundo limite 
limite = Limit(funcao(x), x, S.Infinity).doit()
print('Limite da função para x tendendo a infinito positivo: ')
print(limite, "\n")

#Cálculo do terceiro limite 
limite = Limit(funcao(x), x, -S.Infinity).doit()
print('Limite da função para x tendendo a infinito negativo: ')
print(limite, "\n")