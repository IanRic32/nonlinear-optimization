"""==================================================
 Nombre del archivo:  Max_pend_Newton.py
 Algoritmo de máxima pendiente usando el metodo de Newton para calcular el tamaño de paso.
 Se detiene cuando la norma del gradiente es menor que 'eps1'.

 
 Ejemplo de uso: se define la función que se quiere encontrar su min como 
     def f(v):
         global eval_f   #esta variable controla el número de evaluaciones de f. Es global
                         porque se modifica dentro de otras funciones
        f=f(v[0],v[1],...])
        eval_f+=1
         return f, eval_f
     donde v es un vector de coordenadas ej. v=[2,3,5]
     
     
     Ej. def f_xy(var):
     global eval_f
     eval_f+=1
     f=var[1]*var[0]+50*var[0]**(2)+20*var[1]**(2)
     return f;
 
    Llamar a la fución como max_pend_newton(f_xy,[2,3],.001)
 ===================================================="""
#from math import * #importamos todas las funciones de la librería math
import numpy as np  #importamos la librería numpy para el manejo de vectores y matrices
iter_desc = 0;   """Definimos el numero de iteraciones y evaluaciones como variables globales 
                    ya que se usan dentro de varias funciones distintas"""
iter_alph = 0
eval_f = 0
def max_pend_newton (f,x0,eps): #Creamos la función para el algoritmo de pendiente máx
    global iter_desc
    global iter_alph
    global eval_f
    h = 0.01 # parámetro para las diferencias finitas
    fx0 = f(x0)
    gx0 = grad(f,x0,h) #cálculo del gradiente hecho en una función aparte
    eps2=eps*0.001;  """el valor de fp_nu(x0) llega a ser tan pequeño (menor que la 
    tolerancia eps) que provoca que el código se cicle por cómo está definida
    la funcion NewtonR, por eso eps2 (tolerancia de NewtonR)
   es una centesima parte de eps"""
    while (np.linalg.norm(gx0) > eps):
        nu = -1*gx0               # Dirección de descenso.
        f_nu = lambda x: f(x0+x*nu)          # Composición de la funcion 
        fp_nu = lambda x: DifFin1(f_nu,x,h);  """Se construye la derivada para sacarle su raíz
                                                en este caso usamos una función anónima lambda"""
        alpha = NewtonR(fp_nu,0.1,eps2,h); """#Estimacion del tamaño de paso. 
                                        la raiz de la derivada se obtiene con la función NewtonR
                                        """
        xmin = x0 + alpha*nu;           #calculamos el nuevo punto para el método
        fxmin = f(xmin);                #calculamos f en el nuevo punto
        x0 = xmin;                      #reasignamos los valores para empezar nuevamente el ciclo
        fx0 = fxmin;
        gx0 = grad(f,xmin,h)
        iter_desc +=1                #contador para el núm de veces que entra al método de pend_max
        print("\n",iter_desc, "",xmin,"")
        if iter_desc>50:
            break
    return xmin,fxmin,iter_desc,iter_alph,eval_f;
    #Retorna el punto crítico, su valo bajo f, iteraciones del metodo de max_pend,
    #, iteraciones 
#--------------------------------------------------------------------------
def DifFin1(f,xdf,h):               #Función que calcula las diferencias finitas
    df=(f(xdf+h)-f(xdf-h))/(2*h)    #fórmula diferencias centradas
    return df
#--------------------------------------------------------------------------
def grad(f,xg,h):         #función que calcula el grafiente
    idt=h*np.eye(len(xg)) #creamos una matriz identidad que nos ayudará 
                               #a calcular las darivadas parciales numéricas
    g=np.array([]) #g es el vector gradiente pero inicialmente lo declaramos vacío
    for i in range(len(xg)): #este ciclo calcula cada entrada del vactor gradiente
       g = np.append(g,(f(xg+idt[i])-f(xg-idt[i]))/(2*h)) # Formula de Diferencias Finitas
    return g
#--------------------------------------------------------------------------
def NewtonR(f,x,eps,h):  #función que halla la raiz de fp_nu, usanda el metodo de Newton Raphson
    global iter_alph     #suma las iters de todas las veces que se entró a newton raphson
    i=0                  #i controla que el método de newton no diverja
    xnr=x
    x1=0
    while (abs(f(xnr))>eps): #algoritmo para hallar la raiz
        x1 = xnr-(f(xnr)/DifFin1(f,xnr,h))
        xnr = x1
        iter_alph=iter_alph+1   #el numero iteraciones del tamaño de paso
        i+=1
        if i>50:    #si i>0, salir del método
            break
    return x1;

##########################################################################

def f_xy_1(var):
    global eval_f
    eval_f+=1
    f=8*var[0]**2+4*var[0]*var[1]+5*var[1]**2
    return f;

def f_xy_2(var):
    global eval_f
    eval_f+=1
    f=2*var[0]**3+4*var[0]*var[1]**3-10*var[0]*var[1]+var[1]**2
    return f;

def f_xy_3(var):
    global eval_f
    eval_f+=1
    f = 2*var[0]**2 - 1.05*var[0]**4 + (var[0]**6)/6 + var[0]*var[1]+var[1]**2
    return f;

def f_xy_4(var):
    global eval_f
    eval_f+=1
    f=(var[0]+2*var[1]-7)**2 +(2*var[0]+var[1]-5)**2
    return f;


max_pend_newton(f_xy_4,[3,4],0.00001)