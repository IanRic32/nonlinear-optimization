# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:22:26 2021

@author: riosv
"""
import numpy as np #importamos numpy para hacer el manejo de matrices

grd=0

def grad(f,x0,h):         #funcion que calcula el grafiente
    global grd  #creamos la variable contador gradiente
    
    idt=h*np.eye(len(x0)) #creamos una matriz identidad. 
                          #Nos ayudara a calcular las deriv parciales numÃ©ricas
    g=np.zeros(len(x0))   #g es el vector gradiente pero inicialmente lo declaramos vacÃ­o

    for i in range(len(x0)):   #este ciclo calcula cada entrada del vactor gradiente
        g[i] = (f(x0+idt[i])-f(x0-idt[i]))/(2*h) # Formula de Diferencias Finitas
    grd+=1  #incrementamos el valor del gradiente en cada entrada a la funcion 
    
    return g

