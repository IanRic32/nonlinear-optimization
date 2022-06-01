# nonlinear-optimization
## In this respositori can view methods of nonlineal programming
### first method: Golden Section
with this method can gets the optimous point of a problem of an problem for a enterprise, for example, can be a transport rout with variables like time, fueld, money, etc. therefore if we use this method the enterprise can reduce the costs



###########metodo de la seccion dorada #########################################
from math import* #importamos la libreria math
from numpy import* #importamos la libreria para calculos numericos de numpy
from pylab import* #importamos la libreria de pylab
from sympy import* #importamos la libreria sympy para hacer evaluacion numerica
from pandas import* #importamos la libreria de pandas para hacer el Data Frame
import time #importamos el tiempo
x=Symbol("x") #donde veamos a x, lo sustituiremos por una funcion de x
while True: #mientras sea cierto se piden los siguientes datos
    try:  #el intento de pedir los datos
        a=float(input("Ingresa el limite inferior del intervalo:\t")) #pedimos el limite inferior
        b=float(input("Ingresa el limite superios del intervalo:\t")) #pedimos el limite superior
        gi=sympify(input("Ingresa la tolerancia:\t")) #pedimos la tolerancia
        fx=sympify(input("Ingresa la función:\t")) #pedimos la funcion
        break #rompemos el ciclo si todo es correcto
    except: 
        print("Ingresa de manera correcta los datos por favor") #imprime el error
L=b-a #longitud del intervalo
tau=(-1+pow(5,1/2))/2 #calculamos a tau
x1=b-tau*L #calculamos el valor inicial de x1
x2=a+tau*L #calculamos el valor inicial de x2
LL=[]#creamos la lista vacia para L
fxi=[fx.subs(x,x1)] #agregamos el valor f(x1) en una lista 
fx2i=[fx.subs(x,x2)]  #agregamos el valor f(x2) en una lista 
LL.append(L)  #agregamos el primer valor de L   en una lista
xi=[x1] #aqregamos el valor de x1   en una lista
x2i=[x2] #agregamos el valor inicial de x2   en una lista
while L>=gi:#mientras L sea mmayor o igual al error ingresado hara lo siguiente
    inicio=time.time()#creamos la variable que calcula el tiempo de ejecucion
    if fx.subs(x,x1)<fx.subs(x,x2): #condicion de que f(x1) sea menor que f(x2)
        b=x2 #cambiamos el valor de b por el de x2
        x2=x1 #cambiamos el valor de x2 por x1
        L=b-a #agregamos el error a la lista de LL
        x1=b-tau*L #calculamos a x1
        LL.append(L) #agregamos los errores nuevos en una lista
    else: #si no se cumple la condicion entonces
        a=x1 #cambiamos el valor de a por x1
        x1=x2 #cambiamos el valor de x1 por x2
        L=b-a #calculamos a L
        x2=a+tau*L   #x2
        LL.append(L)#agregamos los errores nuevos en una lista
    fxi.append(fx.subs(x,x1)) #agregamos cada resultado de la funcion evaluada en  x1 en una lista
    fx2i.append(fx.subs(x,x2))   #agregamos cada resultado de la funcion evaluada en  x2 en una lista
    xi.append(x1)  #agregamos cada resultado de la iteracion de x1 en una lista
    x2i.append(x2) #agregamos cada resultado de la iteracion de x2 en una lista
    fin=time.time()#creamos la variable que calcula el tiempo de ejecucion
it=[]#lista vacia de iteraciones
d=0 #contdor
for i in LL: #nos movemos a través de la lista xm, para generar las iteraciones
    d+=1 #agregamos un contador
    it.append(d) #agregamos el contador a una lista para la iteracion
df=DataFrame()#creamos el data frame, para hacer las tablas de evaluacion
df["Iteración"]=it #agregamos la columna iteracion a nuesto Data frame
df["x1"]=xi #agregamos la columna x1 a nuesto Data frame
df["x2"]=x2i #agregamos la columna x2 a nuesto Data frame
df["f(x1)"]=fxi  #agregamos la columna f(x1) a nuesto Data frame 
df["f(x2)"]=fx2i  #agregamos la columna f(x2) a nuesto Data frame
df["Error"]=LL  #agregamos la columna de error a nuesto Data frame con los valores de la lista de L
rl=xi[-1] #buscamos el ultimo elemento de la lista de x1
rl2=x2i[-1] #buscamos el ultimo elemento de la lista de x2
rl3=fxi[-1] #buscamos el ultimo elemento de la lista de f(x1)
rl4=fxi[-1] #buscamos el ultimo elemento de la lista de f(x1)
rrrr=min(rl3,rl4)  #buscamos minimo de las evaluaciones de las f, para ver cual es valor optimo
print("El punto optimo se encuentre en el intervalo ({},{})".format(rl,rl2)) #imprimimos el intervalo donde esta el punto optimo
print("La función evaluada en el punto óptimo es:\t{}".format(fx.subs(x,rl))) #imprimis el valor de la funcion evaluada en el punto optimo
print("Tiempo de ejecucion:\t {} segundos".format((fin-inicio)))#imprimimos el valor de del tiempo de ejecucion del programa
df#imprimimos el Data Frame
