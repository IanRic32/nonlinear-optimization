"""==================================================
 Nombre del archivo:  Max_pend_Inter_mitad.py
 Algoritmo de máxima pendiente usando el metodo de Elim regiones (Invervalos x la mitad)
 para calcular el tamaño de paso.
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
 
    Llamar a la fución como max_pend__inter_mitad(f_xy,[2,3],eps,delx)
        donde delx es el tamaño de paso para la fase de acotamiento
 ===================================================="""
#from math import * #importamos todas las funciones de la librería math
import numpy as np  #importamos la librería numpy para el manejo de vectores y matrices

global iter_desc   
global iter_alph 
global eval_f 
"""Definimos el numero de iteraciones y evaluaciones como variables globales 
   ya que se usan dentro de varias funciones distintas"""
   
def max_pend_inter_mitad (f,x0,eps,delx): #Creamos la función para el algoritmo de pendiente máx
    global iter_desc
    global iter_alph
    global eval_f
    iter_desc = 0;   
    iter_alph = 0
    eval_f = 0
    h = 0.01 # parámetro para las diferencias finitas
    fx0 = f(x0)
    gx0 = grad(f,x0,h) #cálculo del gradiente hecho en una función aparte  
    
    while (np.linalg.norm(gx0) > eps):
        nu = -1*gx0               # Dirección de descenso.
        f_nu = lambda x: f(x0+x*nu)          # Composición de la funcion 
        
        #Acotamiento del intervalo
        I = Fase_acot(f_nu,0.1,delx)
        
        if I==0:
            print("\n No se puede hallar el óptimo de f_nu con el Met de Intervalos x la mitad")
            print("\n No se encontro un intervalo que acote el óptimo")
            print("\n No se encontro un intervalo donde f_nu sea unimodal")
            return False
        else:
            alpha = Inter_mitad(f_nu,I[0],I[1],eps)
            xmin = x0 + alpha*nu;           #calculamos el nuevo punto para el método
            fxmin = f(xmin);                #calculamos f en el nuevo punto
            x0 = xmin;                      #reasignamos los valores para empezar nuevamente el ciclo
            fx0 = fxmin;
            gx0 = grad(f,xmin,h)
            iter_desc +=1               #contadr para el núm de veces que entra al método de pend_max
            print("\n",iter_desc, "",xmin,"")
        
        if iter_desc>50:
            break
        
    return xmin, fxmin, iter_desc, iter_alph, eval_f;
    #Retorna el punto crítico, su valo bajo f, iteraciones del metodo de max_pend,
    #, iteraciones 

#--------------------------------------------------------------------------
def grad(f,xg,h):         #función que calcula el grafiente
    idt=h*np.eye(len(xg)) #creamos una matriz identidad que nos ayudará 
                               #a calcular las darivadas parciales numéricas
    g=np.array([]) #g es el vector gradiente pero inicialmente lo declaramos vacío
    for i in range(len(xg)): #este ciclo calcula cada entrada del vactor gradiente
       g = np.append(g,(f(xg+idt[i])-f(xg-idt[i]))/(2*h)) # Formula de Diferencias Finitas
    return g
#--------------------------------------------------------------------------
def Fase_acot(f,x0,delx):
    """Regresa el intervalo que acota al óptimo de la función f 
    ENTRADA x0: punto inicial cualquiera, delx: incremento de prueba"""
    global eval_f;
    global iter_alph
    
    k = 0;               # Contador de iteraciones
    xL=x0 - abs(delx)
    fxL = f(xL);         # Imagen a la izquierda de x0
    fx0 = f(x0);   
    xR=x0 + abs(delx)                # Imagen de x0
    fxR = f(xR);         # Imagen a la derecha de x0
    b = True;                        # Auxiliar de la busqueda del intervalo
#Primer paso: Determinar el signo de Delta
    if (fxL > fx0) and ( fx0 > fxR) :      #Busqueda en la derecha del punto
        delx = abs(delx);                       
    elif (fxL < fx0) and (fx0 < fxR) :  #Busqueda en la izquierda del punto
        delx = -abs(delx);
    elif (fxL >= fx0) and (fx0 <= fxR):  #Condicion de paro
        I = [xL,xR]; return I   #si ocurre esta situación, el minimo se encuentra
                                #en I, así que la función acaba y retorna I
    else:                               #No hay dirección de búsqueda
        b=False
    #print(delx)    
    xk = x0; #EStos son los primemos puntos de la iteración xk+1=xk+2**k(del)
    xk1 = xk + (2**k)*delx;
    fxk = f(xk);
    fxk1 = f(xk1);
#Segundo paso: Ciclo que se rompe hasta cumplir condicion de paro
    while (fxk>fxk1)and(b): 
        iter_alph +=1    
        k = k+1;
        #print("\n ",k, " I = ",[xk,xk1])
        xk = xk1
        fxk = fxk1;             #Reasignación
        xk1 = xk + (1.2**k)*delx;  #Usamos 1.2**k en vez de 2**k para evitar saltos 
                                   #bruscos en la búsqueda
        fxk1 = f(xk1);
    #print("\n I = ",[xk,xk1])
#Tercer paso: Regresar el valor del intervalo si se entro al ciclo
    if (delx > 0)and(b):
        I = [xk,xk1];
    elif (delx < 0) and (b):
        I = [xk1,xk];
    else:   
        I=False #No se encontró un intervalo de acotamiento.
    return I;

#--------------------------------------------------------------------------
def Inter_mitad(f,a,b,eps):
    """Método de reducción del intervalo por la mitad
     F debe ser unimodal en el intervalo [a,b]
     ENTRADA: f = función a minimizar 
             a,b = intervalo de unimodalidad de f
             eps = precisión deseada del intervalo final
     SALIDA:
         xmin= minimo de f tomado como el punto medio del último intervalo obtenido
      """
    global iter_alph #contador que controla la iteraciones necesarias para 
                        #calcular alpha 
    itr   = 0;          #conta local para Inter_mitad
    xm  = (a+b)/2;      
    fxm = f(xm);
    L   = abs(b-a);
    while (eps<L):      #condiciones para la eliminación de regiones
        itr = itr+1;
        x1 = a+L/4;
        x2   = b-L/4;
        fx1  = f(x1);
        fx2  = f(x2);
        if (fx1 < fxm): #CASO 1
            b  = xm;
            xm = x1;
            fxm = fx1;
        elif (fx2 < fxm): #CASO 2
            a   = xm;
            xm  = x2;
            fxm = fx2; 
        else:              #CASO 3
            a  = x1;
            b  = x2;
            xm=(a+b)/2
        L = abs(b-a)
        if itr>20:   #Por si se cicla
            break;
        iter_alph+=1
        #print("xm =",xm)
    return xm; #devuelve el pto minimo como el pto medio del último interv calculado
    
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

max_pend_inter_mitad(f_xy_3,[2,3],0.0001,0.01)



