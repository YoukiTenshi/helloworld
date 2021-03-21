from . import somsub
from . import muldiv

def printCute(resultado):
    print('Resultado:  ',resultado)

print('Essa é a Calculeira')
calculo = input('O que deseja fazer? Digite: "so" para soma, "su" para subtração, "mu" para multiplicação ou "di" para divisão:  ')

a = input('Insira o primeiro valor:  ')
b = input('Insira o segundo valor:  ')

if calculo = 'so':
    res = somsub.somar(a,b)
    printCute(res)
    
if calculo = 'su':
    res = somsub.subtrair(a,b)
    printCute(res)

if calculo = 'mu':
    res = muldiv.multiplicar(a,b)
    printCute(res)

if calculo = 'di':
    res = muldiv.dividir(a,b)
    printCute(res)
