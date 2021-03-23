from somsub import *
from muldiv import *

def printCute(resultado):
    print('Resultado:  ',resultado)

print('Essa é a Calculeira')
what = input('O que deseja fazer? Digite: "so" para soma, "su" para subtração, "mu" para multiplicação ou "di" para divisão:  ')

a = int(input('Insira o primeiro valor:  '))
b = int(input('Insira o segundo valor:  '))

if what == 'so':
    res = somar(a,b)
    printCute(res)
    
if what == 'su':
    res = subtrair(a,b)
    printCute(res)

if what == 'mu':
    res = multiplicar(a,b)
    printCute(res)

if what == 'di':
    res = dividir(a,b)
    printCute(res)
