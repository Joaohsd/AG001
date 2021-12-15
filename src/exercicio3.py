'''
Nome:       João Henrique Silva Delfino
Matrícula:  1662
Curso:      GEC


Exercício 3 - Cálculo do trabalho realizado por uma força variável

'''

#Importando as funções da biblioteca sympy
from sympy import Integral, Symbol

#Constante
c = 1662%10

def forca(x):
    return (x **(2.0/3.0)) + 3.0 * (x**2.0) + 2 * x - c

#Define x como variável
x = Symbol('x')

#Calculo da integral definida da função que define o valor da força variável.
#A Integral definida tem como limite inferior 0 e limite superior 6
trabalho = Integral(forca(x), (x, 0, 6)).doit()

#Exibindo o trabalho realizado pela força
print("Trabalho realizado pela força entre as posições 0 e 6 metros: ", round(trabalho,3), " [J]")