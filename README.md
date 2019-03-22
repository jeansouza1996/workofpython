# workofpython
-------------------------------------------------------------------------------------------------------------------
Aula (22/02/2019)
Identificadores e função.     

and = e
assert = forçar um tipo para a variavel
break = parar
class = definição da classe
continue = continuar
def = definição de função
del = deleção de objeto
elif = não-se
else = se não
except = exceção
exec = executar função
finally = finalizar função
for = definação de laço para
from = importar uma variavel dentro de um módulo
global = definação de variavel global
if = definição de laço se
import = importação de modulos externos
in = em
is = e
lambda = funções recursivas
not = não
or = ou
pass = passar para outra função sem executá-la
print = imprimir na tela
raise = laço try
return = retornar objeto
try = definição de laço tente
while = definição de laço enquanto 

-------------------------------------------------------------------------------------------------------------------

Aula (01/03/2019)

* principais versões :  Versão 2.7
                        Versão atual 3.7.2

* Conjuntos de ferramentas de desenvolvimento por versão: 
                      
                        visual studio code 2.7 em diante    
                        IDLE python a partir da 1.5.2 em diante



* Diferenças entre as versões : 2.7 e 3.7

                Na versão 3 a função print foi implantada. 
                Na versão 2 a divisão entre inteiros dependia do numerador e do denominador, por exemplo : 3/2 = 1
                Já na versão 3 essa questão foi solucionada havendo um resultado exato, por exemplo : 3/2 = 1,5
                Na versão 3 as palavras true e false se tornaram reservadas. 
                Na versao 2.6 houve implementação do JSON e bibliotecas para multiprocessamento. 
                Na versão 2 era possivel comparar uma variavel texto com variavel numerica. 

-------------------------------------------------------------------------------------------------------------------
Aula (08/03/2019)
tipos primitivos python - 

int - para números inteiros
str - para conjuntos de caracteres
bool -  armazena true ou false
float(32bits)/double(64bits) - numeros decimais 

tipos compostos

tuplas,listas,dicionarios e conjuntos

tupla - semelhante ao tipo list, porém, imutavel
dic - para agrupar elementos que serao recuperados por uma
list - para agrupar um conjunto de elementos



exemplos de codigo do professor = https://www.onlinegdb.com/r1hzaBJvV
                          lists=  https://www.onlinegdb.com/B1sbW81DE
                          turple= https://www.onlinegdb.com/rJrzz8JDE
                          sets=   https://www.onlinegdb.com/HJ5x7UyPV
                dictionaries=     https://www.onlinegdb.com/ryn_m8kPN



exemplos de conversores: 

convertendo string em data

**************************************************************
 from datetime import datetime                                  
                                                               
str_date = '11/07/2018'                                        
                                                               
date = datetime.strptime(str_date, '%d/%m/%Y').date()   

print(date, type(date))

str_date = '2018-07-11'

date = datetime.strptime(str_date, '%Y-%m-%d').date()

print(date, type(date))
************************************************************

Convertendo String em numero:

num = input("Introduza um numero") #'123'
str(num)
print(num)

************************************************************

# Python code to demonstrate Type conversion 
# using int(), float() 
  
# initializing string 
s = "10010"
  
# printing string converting to int base 2 
c = int(s,2) 
print ("After converting to integer base 2 : ", end="") 
print (c) 
  
# printing string converting to float 
e = float(s) 
print ("After converting to float : ", end="") 
print (e)

Exemplos: https://blog.education-ecosystem.com/python-como-transformar-string-para-float-ou-int/

************************************************************
Fluxos de Controle

Else If.

a = 33
b = 33
if b > a:
  print("B é maior do que A")
elif a == b:
  print(" A e B é Igual")

Exemplos: https://www.w3schools.com/python/python_conditions.asp

While.

i = 1
while i < 6:
  print(i)
  i += 1
  
Exemplos: https://www.w3schools.com/python/python_while_loops.asp

************************************************************
Os Exemplos de Else If,Input e Output será demonstrado abaixo nos exercicios. 

Exercício 1

temperaturaCelsius = float(input('Digite a temperatura em graus Celsius \n '))
temperaturaFarenheit = (1.8 * temperaturaCelsius) + 32
print('O valor em Farenheit é de : %.2f' % temperaturaFarenheit)

Exercício 2 

salarioAtual = float(input('Digite o seu salário \n '))
if salarioAtual <= 280 :
    valorAumento = salarioAtual * 0.20
    salarioReajustado = valorAumento + salarioAtual
elif salarioAtual > 280 and salarioAtual <= 700 :
    valorAumento = salarioAtual * 0.15
    salarioReajustado = valorAumento + salarioAtual
elif salarioAtual > 700 and salarioAtual <= 1500 :
    valorAumento = salarioAtual * 0.10
    salarioReajustado = valorAumento + salarioAtual 
elif salarioAtual > 1500 :
    valorAumento = salarioAtual * 0.05
    salarioReajustado = valorAumento + salarioAtual

porcentagemDoAumento = ((salarioReajustado / salarioAtual) - 1) * 100

print('O salário atual deste funcionário é de R$ : %.2f' % salarioAtual)
print('O porcentual de aumento foi de %.0f:' % porcentagemDoAumento)
print('O valor do aumento foi de : %.2f' % valorAumento)
print('O seu novo salário será de R$ : %.2f' % salarioReajustado)


************************************************************

Aula (15/03/2019)

fatorial:
https://trinket.io/python/dc4e7108b6

fatorial usando funções anonimas:


circulo:
https://trinket.io/python/cee3b62314

retangulo:
https://trinket.io/python/feaa7f58d6

base:
https://trinket.io/python/b49c0ef5e0
