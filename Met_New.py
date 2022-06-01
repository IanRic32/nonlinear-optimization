import numpy as np 
from math import sin,pi,cos,sqrt,exp,e,nan
np.set_printoptions(precision=7) #pedimos que el formato de impresión tenga hasta 4 decimales
eval_f=0
hessianaa=0
gradientee=0
def Met_New(f,x0,eps):
    global eval_f
    global a
    
    n=len(x0)
    it_new = 0        # número de iteraciones del método
    h = 1e-8 # parámetro para las diferencias finitas
    xk=x0
    gxk = grad(f,x0,h) #cálculo del gradiente en el punto x0
    while (np.linalg.norm(gxk) >= eps): #condición de paro
        H=Hess(f,xk,h)           #calculamos la matriz hessiana en el punto x0
        
        try: #Sentencia Try-except para controlar los errores de tipo SingularMatrix
            #dk=np.linalg.pinv(H)@(-gxk).reshape(n,1)
            dk=np.dot(np.linalg.pinv(H),-gxk)

            dk=dk.reshape(n)    #resolvemos el sistema H*dk=-grad
            xk_1 = xk + dk             #calculamos el nuevo punto x^k+1
            xk=xk_1      #reasignamos los valores
            gxk = grad(f,xk,h)
            it_new +=1              #contador para el núm de veces que entra al método
            
        except:
            print(it_new, " xk=", xk, " f=", format(f(xk),".9f"),"\n " )
            #a=[it_new,"SingularMatrx",nan,evalf]
            #return a
            raise
        
        if it_new>100:
            break
    a=np.array([it_new,xk_1,f(xk_1),eval_f,gradientee,hessianaa])
    print("\n ", a,"\n " )
    eval_f=0
    return a
 #======================================================================================
   
def Hess(f,x0,h):
    global hessianaa
    hessianaa+=1
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
#====================================================================================

def grad(f,x0,h):         #funcion que calcula el grafiente
    global gradientee
    
    idt=1/2*h*np.eye(len(x0)) #creamos una matriz identidad que nos ayudará 
                               #a calcular las darivadas parciales numéricas
    g=np.zeros(len(x0)) #g es el vector gradiente pero inicialmente lo declaramos vacío

    for i in range(len(x0)):   #este ciclo calcula cada entrada del vactor gradiente
        g[i] = (f(x0+idt[i])-f(x0-idt[i]))/(h) # Formula de Diferencias Finitas
    gradientee+=1
    return g
#====================================================================================
"""
def Rosnbrk5 (x):
    global evalf
    evalf+=1
    f=0
    for ii in range(5-1):
    	xi = x[ii]
    	xnext = x[ii+1]
    	new = 100*(xnext-xi**2)**2 + (xi-1)**2;
    	f = f + new;     
    return f

X=[25,12,-50,0,-33/10]

a2=Met_New(Rosnbrk5, X ,.001)
"""
"""
evalf=0
def f2 (x):
    global evalf
    evalf+=1
    f = x[0]**2 + exp(x[1]/10+10) + sin(x[1]*x[2])
    return f

X2=[-1/4,1/4,2201]

a22=Met_New(f2, X2 ,.001)
"""

"""
def Rosnbrk3 (x):
    global evalf
    evalf+=1
    f=0
    for ii in range(3-1):
    	xi = x[ii]
    	xnext = x[ii+1]
    	new = 100*(xnext-xi**2)**2 + (xi-1)**2;
    	f = f + new;     
    return f

X3=[50,50,50]

a23=Met_New(Rosnbrk3,X3,.001)
"""

"""
def f_1(x):
    global eval_f
    f = 100*(x[0]**2-x[1])**2+ (1 - x[0])**2
    eval_f=eval_f+1
    return f

def f_2(x):
    global eval_f
    eval_f+=1
    f = (x[0]**2 - x[1])**2 + (1 - x[0])**2
    return f

def f_3(x):
    global eval_f
    eval_f+=1
    f = (x[0]**2 - x[1])**2 + 100*(1 - x[0])**2
    return f

def f_4(x):
    global eval_f
    eval_f+=1
    f = 100*(x[0]**3 - x[1])**2 + (1 - x[0])**2
    return f

"""

"""
def f1(x):
    global eval_f
    f = 100*(x[0]**2-x[1])**2 + (1 - x[0])**2
    eval_f=eval_f+1
    return f;
"""
def funcion(x):
    global eval_f
    #f = 100*(-x[0]**2+x[1])**2 + (1 - x[0])**2
    #f=(1-x[0])**2+(1-x[1])**2+100*(-x[0]**2+x[1]**2)**2+(1-x[2])**2+100*(-x[1]**2+x[2])**2+100*(-x[2]**2+x[3])**2
    #f=8*x[0]**2+4*x[0]*x[1]+5*x[1]**2
    #f=x[0]**3 - x[0]*x[1] + x[1]**2 - 2*x[0] + 3*x[1] - 4
    #f=x[0]**2+exp(x[1]/10+10)+sin(x[1]*x[2])
    #f=(-1+x[0])**2+100*(x[0]**2-x[1])**2+(-1+x[1])**2+100*(x[1]**2-x[2])**2+(-1+x[2])**2+100*(x[2]**2-x[3])**2+(-1+x[3])**2+100*(x[3]**2-x[4])**2+(-1+x[4])**2+100*(x[4]**2-x[5])**2+(-1+x[5])**2+100*(x[5]**2-x[6])**2+(-1+x[6])**2+100*(x[6]**2-x[7])**2+(-1+x[7])**2+100*(x[7]**2-x[8])**2+(-1+x[8])**2+100*(x[8]**2-x[9])**2
    f=x[0]**2+2*x[1]**2+3*x[2]**2+4*x[3]**2+(x[0]+x[1]+x[2]+x[3])**2
    eval_f+=1
    return f
x0=np.array([10,10,10,10])

Met_New(funcion,x0,1e-10)

print("Iteraciones:\t",a[0],"\n\nPunto Optimo:\t",a[1],"\n\nEvaluacion del Optimo:\t",a[2],
      "\n\nLLamadas a la funcion:\t",a[3],"\n\nLLamadas al gradiente:\t",a[4],"\n")