#!/usr/bin/env python

# coding: utf-8

# In[ ]:


print("\n******************* Python Calculator *******************")


print("\nSelecione o Numero da Operacão Desejada:\n")

def soma(a,b):
    return a+b
def Sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divi(a,b):
    return a/b

print('1- Soma')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')

c= input ('\nEscolha uma opção 1/2/3/4:')
if c >'4':
    print('Opção Invalida')
    
num1 = int(input('\nDigite o primeiro Numero: '))
num2 = int(input('Digite o Segundo Numero: ')) 
    
if c == '1':
    print('Resultado:', soma(num1,num2))
if c == '2':
    print('Resultado:',Sub(num1,num2))
if c == '3':
    print('Resultado:',mult(num1,num2))
if c == '4':
    print('Resultado:',divi(num1,num2))

    

