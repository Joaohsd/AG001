'''
Nome:       João Henrique Silva Delfino
Matrícula:  1662
Curso:      GEC


Exercício 5 - Solução de equações

'''

#Importando as funções da biblioteca sympy
from sympy import Symbol, solve, tan

#Constante
c = 1662%10

#Definição das funções a serem resolvidas
def equacao_1(x):
    return (2**x) + (2 ** (4*x)) - c - 1

def equacao_2(x):
    return 5*(x**(1.0/2.0)) -(4 * (x**2)) + (x/2.0) - c

def equacao_3(x):
    return ((3*(tan((c-3)*x))+2)**2)

#Define x como variável
x = Symbol('x')

primeira_equacao = equacao_1(x)
segunda_equacao = equacao_2(x)
terceira_equacao = equacao_3(x)

#Resolução das equações
solucao_1 = solve(primeira_equacao)
solucao_2 = solve(segunda_equacao)
solucao_3 = solve(terceira_equacao)

#Exibição dos resultados
print("Equação 1: ", solucao_1, "\n")
print("Equação 2: ", solucao_2, "\n")
print("Equação 3: ", solucao_3, "\n")
