# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 14:50:02 2021

@author: riosv
"""

import numpy as np
def Hess(f,x0,h):
    Id=h*np.eye(len(x0)) #matriz identdad que nos ayudará a calcular las darivadas parciales numéricas
    H=np.zeros((len(x0),len(x0))) #matriz Hessiana tamaño len(x0)xlen(x0), al inicio está vacía
    #calculamos H en dos pasos, primero las entradas fuera de la diag y luego en la diagonal
    for i in range(0,len(x0)-1):            #este ciclo recorre las filas de H   
        for j in range(i+1,len(x0)):    #este ciclo llena las entradas de H que son derivada cruzada 
                                        # y que están encima de la diagonal 
            H[i,j]= (f(x0+Id[i]+Id[j])-f(x0+Id[i]-Id[j])-f(x0-Id[i]+Id[j])+f(x0-Id[i]-Id[j])) / (4*h**2)
                              #formula dif finitas para derivadas cruzadas
    
    H=H+np.transpose(H)                 #aprovecahmos la propiedad de que H es simétrica para 
                                        #llenar las demás entradas abajo de la diagonal
    for i in range(len(x0)): 
    #este for recorre la diagonal de H, calcula la 2da deriv respecto a la variable x_i
        H[i,i]= (f(x0+Id[i]) -2*f(x0) +f(x0-Id[i])) / (h**2)    
    return H 