# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:29:16 2021

@author: riosv
"""

#recibimos k=0,g0,d0=-g0

#d0=-g0=Qx0-b
import numpy as np
from pandas import*
Q=[[1,2,3],[2,5,6],[3,6,0]]
x=[1,0,-1]
b=[2,12,4]
d0=-(np.dot(Q,x)-b)
g0=-d0
x0=x

"""
k=0

while g.all()!=0:
    gt=np.transpose(g)
    ff=np.dot(gt,d)
    dt=np.transpose(d)
    fr=np.dot(dt,np.dot(Q,d))
    alpha=-(ff)/(fr)
    x1=x+np.dot(alpha,d)
    
print(g.all()!=0,"\n",x1)
"""
d=d0
g=g0
k=0
dd=[]
gg=[]
while np.linalg.norm(g)>=1*10**(-10):
    if g.all()!=0:
        ak=-(np.dot((np.transpose(g)),d))/(np.dot(np.transpose(d),np.dot(Q,d)))
        xk=x+np.dot(ak,d)
        g=-(-(np.dot(Q,xk)-b))
        #k+=1
        x=xk
        
        if np.linalg.norm(g)==0:
            #print("esto en el if","\ngradiente:\t",g)
            break
        else:
            bk=np.dot(np.transpose(g),np.dot(Q,d))/(np.dot(np.transpose(d),np.dot(Q,d)))
            d=-g+np.dot(bk,d)
            #k+=1
            #print("Estoy en el else","\ngradiente:\t",g)
        d0=d
        g0=g
        dd.append(d0)
        gg.append(g)
    k+=1    #k+=1
df=DataFrame()
df['dk']=dd
df['gk']=gg
print("x0:\t",x0,"\ndk=\t",d0,"\ngk=\t",g0,"\npunto\t",xk,"\niteraciones\t",k)
#print(df)