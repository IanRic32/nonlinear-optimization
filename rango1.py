# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:23:22 2021

@author: riosv
"""
import numpy as np #se importa la libreria numpy
from pandas import * #se importa la libreria pandas
import gradiente as gradi #se importa el modulo gradiente 
grd=0
eval_f=0 #iniciamos la variable

def funcion(x):
    global eval_f  #variable gloabl eval_f
    #f = 100*(-x[0]**2+x[1])**2 + (1 - x[0])**2
    #f=(1-x[0])**2+(1-x[1])**2+100*(-x[0]**2+x[1]**2)**2+(1-x[2])**2+100*(-x[1]**2+x[2])**2+100*(-x[2]**2+x[3])**2
    #f=8*x[0]**2+4*x[0]*x[1]+5*x[1]**2
    #f=x[0]**3 - x[0]*x[1] + x[1]**2 - 2*x[0] + 3*x[1] - 4
    #f=x[0]**2+exp(x[1]/10+10)+sin(x[1]*x[2])
    f=(-1+x[0])**2+100*(x[0]**2-x[1])**2+(-1+x[1])**2+100*(x[1]**2-x[2])**2+(-1+x[2])**2+100*(x[2]**2-x[3])**2+(-1+x[3])**2+100*(x[3]**2-x[4])**2+(-1+x[4])**2+100*(x[4]**2-x[5])**2+(-1+x[5])**2+100*(x[5]**2-x[6])**2+(-1+x[6])**2+100*(x[6]**2-x[7])**2+(-1+x[7])**2+100*(x[7]**2-x[8])**2+(-1+x[8])**2+100*(x[8]**2-x[9])**2
    #f=x[0]**2+2*x[1]**2+3*x[2]**2+4*x[3]**2+(x[0]+x[1]+x[2]+x[3])**2
    eval_f+=1  #incrementamos el valor la variable cada que entramos a la funcion
    return f  #retornamos el la funcion f

def Quasi_New1(f,x0,eps):
    global eval_f #variable global evaluaciones de f
    global poptimo  #variable global poptimo 
    global fpoptimo  #variable global evaluacion del optimo
    global grd
    global a
    k = 0        # numero de iteraciones del método
    n=len(x0)  #longitud del punto inicial 
    h = 1e-6 #tamaño de paso de h
    xk_1=x0  #tenemos que el punto xk+1 es xk
    poptimo=[]   #lista vacia de puntos optimos
    fpoptimo=[]  #lista vacia de evaluacion de puntos optimos
    gk_1=gradi.grad(f,x0,h)  #nombramos al gradiente de xk+1
    Hk_1=np.eye(n)
 #   print("\n",gk_1,"\n",Hk_1)
    while (np.linalg.norm(gk_1) >= eps): #condicion de paro
        xk = xk_1   #Reasignamos valores de xk+1
        gk = gk_1   #Reasignamos valores de g(xk+1)
        Hk = Hk_1   #Reasignamos valores de H(xk+1)
        dk=(-np.dot(Hk,gk))/np.linalg.norm(np.dot(Hk,gk)) #Direccion de descenso
        fnu = lambda y: f(xk+y*dk)      #funcion restringida a la direccion dk
        alpha = 1/2 ; rho= 1/2 ; c= 3/10   #Parametros Backtrackin'Armijo
        while fnu(alpha)>f(xk)+c*alpha*(gk.dot(dk)):
            alpha=rho*alpha                #Reasignamos valores de alpha
        xk_1=xk+alpha*dk    #xk+1 es igual a xk+alpha*dk
        gk_1=gradi.grad(f,xk_1,h)   #calculamos el gradiente de g(xk+1)
        
        if np.linalg.norm(gk_1)>= eps: #condicional de que la norma del gradiente sea mayor o igual
            #al error
            if k % (n+1) == 0 or (gk_1==gk).all(): #si el modulo de k es igual a 0 o 
                #g(xk+1)=g(xk) en cada elemento entonces 
                Hk_1=np.eye(n)  #la hesiana H(xk+1) unos
                #dk=-gk
            else:
                delX=xk_1-xk          #delta de x es la diferencia de xk+1-xk
                delG=gk_1-gk      #delta de g= g(k+1)-g(k)
                if np.dot( np.transpose(delX),delG )==0:
                    Hk_1=np.eye(n)
                else:
                    Hk_1=Hk+(((delX-Hk@delG).reshape(n,1))@((delX-Hk@delG).reshape(1,n))/ (delG@(delX-Hk@delG)))
                """
                Hk_1=Hk+ ( (delX-(np.dot(Hk,delG))) ( np.transpose( (delX-(np.dot(Hk,delG) ) ) ) ) )/( np.dot( np.transpose(delG) , (delX-(np.dot(Hk,delG))) ) ) #calculamos la nueva hessiana
                #print("Hk_1",Hk_1)
                """
        k +=1 #incrementamos a k
        poptimo.append(xk_1) #agregamos a la lista el valor de xk+1
        fpoptimo.append(f(xk_1))    #agregamos a la lista el valor de la evaluacion de xk+1
        if k>635: #si k >200
            break #rompemos el ciclo

    a=np.array([k,xk_1,f(xk_1),eval_f,gradi.grd]) #creammos el vector que imprime los datos
    eval_f=0
    gradi.grd=0
    return a #retornamos el vector con la informacion
#x0=[1,2,3,4,5,6,7,8,9,10]
Quasi_New1(funcion,[1,2,3,4,5,6,7,8,9,10],1e-9) #corremos el metodo
df=DataFrame() #creamos el data frame
df['P optimo']=poptimo #imprimimos la columna de puntos optimos con el vector de poptimo 
df['Eval P optimo']=fpoptimo  #imprimimos la columna de eval de puntos optimos con el vector de poptimo
#print(df)#imprimimos el data frame
print("Iteraciones:\t",a[0],"\nPunto óptimo:\t",    a[1],"\nevaluacion del optimo:\t",a[2],"\nLLamadas a la funcion:\t",a[3],"\nLLamadas al gradiente\t",a[4])
