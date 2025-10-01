# 🐍 Implementaciones de Algoritmos de Optimización en Python

Este documento contiene varias implementaciones en Python de algoritmos fundamentales de optimización sin restricciones, utilizando `numpy` para el álgebra lineal y `pandas` para el manejo de resultados.

## 1\. Módulo Auxiliar `gradiente` (`gradiente.py`)

Este módulo se encarga de calcular el gradiente de una función multivariable utilizando diferencias finitas centradas.

```python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:22:26 2021

@author: riosv
"""
import numpy as np # importamos numpy para hacer el manejo de matrices

grd = 0 # Contador global para las llamadas al gradiente

def grad(f, x0, h):         # funcion que calcula el gradiente
    global grd  # creamos la variable contador gradiente
    
    idt = h * np.eye(len(x0)) # creamos una matriz identidad.
                              # Nos ayudara a calcular las deriv parciales numéricas
    g = np.zeros(len(x0))   # g es el vector gradiente

    for i in range(len(x0)):   # este ciclo calcula cada entrada del vector gradiente
        g[i] = (f(x0 + idt[i]) - f(x0 - idt[i])) / (2 * h) # Formula de Diferencias Finitas
    
    grd += 1  # incrementamos el valor del gradiente en cada entrada a la funcion
    
    return g
```

-----

## 2\. Métodos Cuasi-Newton (BFGS / DFP)

Implementaciones de métodos Cuasi-Newton que usan una aproximación de la inversa de la Hessiana ($H_k$). Se observa que las implementaciones `Quasi_New1`, `Quasi_New2` y `Quasi_New3` usan diferentes fórmulas de actualización.

### Función de Prueba (`funcion(x)`)

Se utiliza una Función de **Rosenbrock** extendida a 10 variables como función objetivo en los ejemplos.

$$f(x) = \sum_{i=1}^{N-1} \left[ (1 - x_i)^2 + 100(x_i^2 - x_{i+1})^2 \right] + (1 - x_N)^2$$

```python
# Contiene la función objetivo para los métodos Cuasi-Newton
from math import *
import numpy as np
from pandas import *
import gradiente as gradi

eval_f = 0
grd = 0

def funcion(x):
    global eval_f
    # Rosenbrock extendida para 10 variables (N=10)
    f = 0
    for i in range(len(x) - 1):
        f += (-1 + x[i])**2 + 100 * (x[i]**2 - x[i+1])**2
    f += (-1 + x[-1])**2 # Último término, asumiendo una forma modificada o un error en la transcripción de la fórmula.
    
    # La fórmula más compacta y probablemente intencionada del código:
    # f=(-1+x[0])**2+100*(x[0]**2-x[1])**2 + ... + 100*(x[8]**2-x[9])**2
    
    eval_f += 1
    return f
```

### 2.1. Método Cuasi-Newton 3 (BFGS Aproximado)

Parece ser una variante del algoritmo **BFGS** (Broyden–Fletcher–Goldfarb–Shanno), especialmente en la estructura de la actualización de $H_k$.

```python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:00:12 2021

@author: riosv
"""
# ... (imports y funcion(x) definidos arriba o en gradiente) ...
# Se asume el uso del módulo 'gradiente' con la función 'grad'.

def Quasi_New3(f, x0, error):
    global eval_f
    global a
    k = 0
    n = len(x0)
    h = 1e-6
    xk_1 = x0
    gk_1 = gradi.grad(f, x0, h)
    Hk_1 = np.eye(n)
    
    while (np.linalg.norm(gk_1) >= error):
        xk = xk_1
        gk = gk_1
        Hk = Hk_1
        
        # Dirección de descenso (normalizada)
        dk = (-np.dot(Hk, gk)) / np.linalg.norm(np.dot(Hk, gk))
        
        # Búsqueda de línea (Backtracking con Regla de Armijo)
        fnu = lambda y: f(xk + y * dk)
        alpha = 1/2 ; rho = 1/2 ; c = 3/10
        while fnu(alpha) > f(xk) + c * alpha * (gk.dot(dk)):
            alpha = rho * alpha
            
        xk_1 = xk + alpha * dk
        gk_1 = gradi.grad(f, xk_1, h)
        
        if np.linalg.norm(gk_1) >= error:
            # Re-inicialización de la Hessiana aproximada (cada n+1 iteraciones o si el gradiente es el mismo)
            if k % (n + 1) == 0 or (gk_1 == gk).all():
                Hk_1 = np.eye(n)
            else:
                delX = xk_1 - xk
                delG = gk_1 - gk
                
                if np.dot(np.transpose(delX), delG) == 0:
                    Hk_1 = np.eye(n)
                else:
                    # Actualización Cuasi-Newton (similar a BFGS)
                    w = np.dot(delX, np.transpose(delX))
                    w2 = np.dot(np.transpose(delX), delG)
                    w3 = np.dot(np.transpose(delG), np.dot(Hk, delG))
                    w4 = np.dot(np.transpose(delG), delX)
                    w5 = np.dot(Hk, np.dot(delG, np.transpose(delX)))
                    
                    # Fórmula de actualización compleja (probablemente DFP o una variante)
                    Hk_1 = Hk + np.dot((1 + w3 / w4), (w / w2)) - (w5 + np.transpose(w5)) / w4
        
        k += 1
        if k > 900:
            break
            
    a = np.array([k, xk_1, f(xk_1), eval_f, gradi.grd])
    eval_f = 0
    gradi.grd = 0
    return a

# Ejecución de prueba
# Quasi_New3(funcion, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1e-9)
# print("Iteraciones:\t", a[0], "\nPunto óptimo:\t", a[1], "\nevaluacion del optimo:\t", a[2], "\nLLamadas a la funcion:\t", a[3], "\nLLamadas al gradiente\t", a[4])
```

### 2.2. Método Cuasi-Newton 2 (DFP o BFGS Simplificado)

Utiliza una fórmula de actualización que se asemeja a una versión simplificada de BFGS o DFP (Davidon–Fletcher–Powell).

```python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:21:34 2021

@author: riosv
"""
# ... (imports y funcion(x) definidos arriba o en gradiente) ...

def Quasi_New2(f, x0, error):
    global eval_f
    global poptimo
    global fpoptimo
    global a
    k = 0
    n = len(x0)
    h = 1e-6
    xk_1 = x0
    poptimo = []
    fpoptimo = []
    gk_1 = gradi.grad(f, x0, h)
    Hk_1 = np.eye(n)
    
    while (np.linalg.norm(gk_1) >= error):
        xk = xk_1
        gk = gk_1
        Hk = Hk_1
        
        # Dirección de descenso (normalizada)
        dk = (-np.dot(Hk, gk)) / np.linalg.norm(np.dot(Hk, gk))
        
        # Búsqueda de línea (Backtracking con Regla de Armijo)
        fnu = lambda y: f(xk + y * dk)
        alpha = 1/2 ; rho = 1/2 ; c = 3/10
        while fnu(alpha) > f(xk) + c * alpha * (gk.dot(dk)):
            alpha = rho * alpha
            
        xk_1 = xk + alpha * dk
        gk_1 = gradi.grad(f, xk_1, h)
        
        if np.linalg.norm(gk_1) >= error:
            # Re-inicialización
            if k % (n + 1) == 0 or (gk_1 == gk).all():
                Hk_1 = np.eye(n)
            else:
                delX = xk_1 - xk
                delG = gk_1 - gk
                
                if np.dot(np.transpose(delX), delG) == 0:
                    Hk_1 = np.eye(n)
                else:
                    # Actualización de Cuasi-Newton (Fórmula DFP/BFGS)
                    w = np.dot(delX, np.transpose(delX))
                    w2 = np.dot(np.transpose(delX), delG)
                    w3 = np.dot(np.dot(Hk, delG), np.dot(Hk, delG)) # Error: debería ser delG^T * Hk * delG
                    w4 = np.dot(np.transpose(delG), np.dot(Hk, delG))
                    
                    # La fórmula es Hk_1 = Hk + (delX*delX^T)/(delX^T*delG) - (Hk*delG*delG^T*Hk^T)/(delG^T*Hk*delG)
                    Hk_1 = Hk + w/w2 - w3/w4 # Esta fórmula es la **DFP** si Hk es la inversa de la Hessiana
        
        poptimo.append(xk_1)
        fpoptimo.append(f(xk_1))
        k += 1
        if k > 900:
            break
            
    a = np.array([k, xk_1, f(xk_1), eval_f - len(fpoptimo), gradi.grd])
    eval_f = 0
    gradi.grd = 0
    return a

# Ejecución de prueba
# Quasi_New2(funcion, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1e-9)
# print(df)
```

### 2.3. Método Cuasi-Newton 1 (SR1 Aproximado)

Esta fórmula se asemeja a la actualización de rango 1 simétrica (**SR1**), aunque implementada de forma simplificada o aproximada.

```python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:23:22 2021

@author: riosv
"""
# ... (imports y funcion(x) definidos arriba o en gradiente) ...

def Quasi_New1(f, x0, eps):
    global eval_f
    global poptimo
    global fpoptimo
    global a
    k = 0
    n = len(x0)
    h = 1e-6
    xk_1 = x0
    poptimo = []
    fpoptimo = []
    gk_1 = gradi.grad(f, x0, h)
    Hk_1 = np.eye(n)
    
    while (np.linalg.norm(gk_1) >= eps):
        xk = xk_1
        gk = gk_1
        Hk = Hk_1
        
        dk = (-np.dot(Hk, gk)) / np.linalg.norm(np.dot(Hk, gk)) # Dirección de descenso
        
        # Búsqueda de línea (Backtracking con Regla de Armijo)
        fnu = lambda y: f(xk + y * dk)
        alpha = 1/2 ; rho = 1/2 ; c = 3/10
        while fnu(alpha) > f(xk) + c * alpha * (gk.dot(dk)):
            alpha = rho * alpha
            
        xk_1 = xk + alpha * dk
        gk_1 = gradi.grad(f, xk_1, h)
        
        if np.linalg.norm(gk_1) >= eps:
            # Re-inicialización
            if k % (n + 1) == 0 or (gk_1 == gk).all():
                Hk_1 = np.eye(n)
            else:
                delX = xk_1 - xk
                delG = gk_1 - gk
                
                if np.dot(np.transpose(delX), delG) == 0:
                    Hk_1 = np.eye(n)
                else:
                    # Actualización Cuasi-Newton (Fórmula SR1)
                    # La fórmula es (delX - Hk*delG) * (delX - Hk*delG)^T / (delG^T * (delX - Hk*delG))
                    Hk_1 = Hk + (((delX - Hk @ delG).reshape(n, 1)) @ ((delX - Hk @ delG).reshape(1, n)) / (delG @ (delX - Hk @ delG)))
        
        k += 1
        poptimo.append(xk_1)
        fpoptimo.append(f(xk_1))
        if k > 635:
            break
            
    a = np.array([k, xk_1, f(xk_1), eval_f, gradi.grd])
    eval_f = 0
    gradi.grd = 0
    return a

# Ejecución de prueba
# Quasi_New1(funcion, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1e-9)
```

-----

## 3\. Método del Gradiente Conjugado (GC)

Implementación del algoritmo de **Gradiente Conjugado** para resolver sistemas cuadráticos de la forma $\min f(x) = \frac{1}{2} x^T Q x - b^T x$.

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:29:16 2021

@author: riosv
"""
import numpy as np
from pandas import *

# Parámetros del sistema cuadrático Qx = b
Q = [[1, 2, 3], [2, 5, 6], [3, 6, 0]]
x = [1, 0, -1] # Punto inicial x0
b = [2, 12, 4]

# Inicialización
d0 = -(np.dot(Q, x) - b) # d0 = -g0
g0 = -d0
x0 = x

d = np.array(d0)
g = np.array(g0)
x = np.array(x0)
k = 0
dd = []
gg = []

# Algoritmo de Gradiente Conjugado
while np.linalg.norm(g) >= 1e-10:
    if np.linalg.norm(g) != 0:
        # Paso de línea (alpha_k)
        ak = -(np.dot(np.transpose(g), d)) / (np.dot(np.transpose(d), np.dot(Q, d)))
        
        # Actualización de x (x_k+1)
        xk = x + np.dot(ak, d)
        
        # Cálculo del nuevo gradiente (g_k+1)
        g = np.array(np.dot(Q, xk) - b)
        
        x = xk # Reasignación para la siguiente iteración
        
        if np.linalg.norm(g) < 1e-10:
            break
        else:
            # Coeficiente beta_k de Fletcher-Reeves
            bk = np.dot(np.transpose(g), np.dot(Q, d)) / (np.dot(np.transpose(d), np.dot(Q, d)))
            
            # Dirección de búsqueda (d_k+1)
            d = -g + np.dot(bk, d)
        
        d0 = d
        g0 = g
        dd.append(d0)
        gg.append(g)
    k += 1

df = DataFrame()
df['dk'] = dd
df['gk'] = gg

print("x0:\t", x0, "\ndk=\t", d0, "\ngk=\t", g0, "\npunto\t", xk, "\niteraciones\t", k)
# print(df)
```

-----

## 4\. Método de Newton con Diferencias Finitas

Implementación del método de **Newton** donde el gradiente y la matriz Hessiana se calculan utilizando aproximaciones por diferencias finitas.

### Funciones Auxiliares: `Hess(f, x0, h)` y `grad(f, x0, h)`

```python
# ... (imports de numpy, math, y np.set_printoptions) ...
import numpy as np
from math import sin,pi,cos,sqrt,exp,e,nan
np.set_printoptions(precision=7)
# ... (definición de eval_f, hessianaa, gradientee) ...

# Matriz Hessiana Numérica
def Hess(f, x0, h):
    global hessianaa
    hessianaa += 1
    Id = h * np.eye(len(x0))
    H = np.zeros((len(x0), len(x0)))
    
    # Derivadas cruzadas (fuera de la diagonal)
    for i in range(0, len(x0) - 1):
        for j in range(i + 1, len(x0)):
            H[i, j] = (f(x0 + Id[i] + Id[j]) - f(x0 + Id[i] - Id[j]) - f(x0 - Id[i] + Id[j]) + f(x0 - Id[i] - Id[j])) / (4 * h**2)
    
    H = H + np.transpose(H) # Simetría
    
    # Derivadas en la diagonal
    for i in range(len(x0)):
        H[i, i] = (f(x0 + Id[i]) - 2 * f(x0) + f(x0 - Id[i])) / (h**2)
    return H

# Gradiente Numérico (diferencias centradas)
def grad(f, x0, h):
    global gradientee
    gradientee += 1
    idt = 1/2 * h * np.eye(len(x0)) # Nota: Se usa h/2 en el paso de diferencias centradas
    g = np.zeros(len(x0))
    for i in range(len(x0)):
        g[i] = (f(x0 + idt[i]) - f(x0 - idt[i])) / (h) # Fórmula con paso h/2.
    return g
```

### Método de Newton

```python
# ... (función Hess y grad definidas arriba) ...

def Met_New(f, x0, eps):
    global eval_f
    global a
    n = len(x0)
    it_new = 0
    h = 1e-8 # parámetro para las diferencias finitas
    xk = x0
    gxk = grad(f, x0, h)
    
    while (np.linalg.norm(gxk) >= eps):
        H = Hess(f, xk, h) # Matriz Hessiana
        
        try:
            # Resuelve H * dk = -gxk (usando pinv para manejar matrices singulares)
            dk = np.dot(np.linalg.pinv(H), -gxk)
            dk = dk.reshape(n)
            
            xk_1 = xk + dk
            xk = xk_1
            gxk = grad(f, xk, h)
            it_new += 1
            
        except:
            print(it_new, " xk=", xk, " f=", format(f(xk), ".9f"), "\n ")
            raise
            
        if it_new > 100:
            break
            
    a = np.array([it_new, xk_1, f(xk_1), eval_f, gradientee, hessianaa])
    print("\n ", a, "\n ")
    eval_f = 0
    return a

# Función de prueba utilizada en el código
def funcion(x):
    global eval_f
    f = x[0]**2 + 2*x[1]**2 + 3*x[2]**2 + 4*x[3]**2 + (x[0] + x[1] + x[2] + x[3])**2
    eval_f += 1
    return f

# Ejecución de prueba
# x0 = np.array([10, 10, 10, 10])
# Met_New(funcion, x0, 1e-10)
# print("Iteraciones:\t", a[0], "\n\nPunto Optimo:\t", a[1], "\n\nEvaluacion del Optimo:\t", a[2], "\n\nLLamadas a la funcion:\t", a[3], "\n\nLLamadas al gradiente:\t", a[4], "\n")
```

-----

## 5\. Método de Máxima Pendiente (con Búsqueda de Línea por Newton-Raphson)

Algoritmo de **Máxima Pendiente** (Gradient Descent) que utiliza el método de **Newton-Raphson** para encontrar numéricamente el tamaño de paso óptimo ($\alpha$) a lo largo de la dirección de descenso.

```python
"""==================================================
 Nombre del archivo: Max_pend_Newton.py
 Algoritmo de máxima pendiente usando el metodo de Newton para calcular el tamaño de paso.
 ===================================================="""
import numpy as np

iter_desc = 0
iter_alph = 0
eval_f = 0

# Función auxiliar: Diferencias Finitas Centradas 1D
def DifFin1(f, xdf, h):
    df = (f(xdf + h) - f(xdf - h)) / (2 * h)
    return df

# Función auxiliar: Gradiente Numérico (Mismo que en Sección 1)
def grad(f, xg, h):
    idt = h * np.eye(len(xg))
    g = np.array([])
    for i in range(len(xg)):
        g = np.append(g, (f(xg + idt[i]) - f(xg - idt[i])) / (2 * h))
    return g

# Función auxiliar: Newton-Raphson para encontrar la raíz de la derivada (alpha)
def NewtonR(f, x, eps, h):
    global iter_alph
    i = 0
    xnr = x
    while (abs(f(xnr)) > eps):
        x1 = xnr - (f(xnr) / DifFin1(f, xnr, h))
        xnr = x1
        iter_alph = iter_alph + 1
        i += 1
        if i > 50:
            break
    return x1

# Método de Máxima Pendiente
def max_pend_newton(f, x0, eps):
    global iter_desc
    global iter_alph
    global eval_f
    h = 0.01 # parámetro para las diferencias finitas
    fx0 = f(x0)
    gx0 = grad(f, x0, h)
    eps2 = eps * 0.001
    
    while (np.linalg.norm(gx0) > eps):
        nu = -1 * gx0 # Dirección de descenso.
        f_nu = lambda x: f(x0 + x * nu) # Función de composición f(x0 + alpha*nu)
        
        # Derivada de f_nu para encontrar su raíz (el alpha óptimo)
        fp_nu = lambda x: DifFin1(f_nu, x, h)
        
        # Estimación del tamaño de paso (alpha)
        alpha = NewtonR(fp_nu, 0.1, eps2, h)
        
        xmin = x0 + alpha * nu # Nuevo punto
        fxmin = f(xmin)
        
        # Reasignación de valores
        x0 = xmin
        fx0 = fxmin
        gx0 = grad(f, xmin, h)
        iter_desc += 1
        
        print("\n", iter_desc, "", xmin, "")
        if iter_desc > 50:
            break
            
    return xmin, fxmin, iter_desc, iter_alph, eval_f

# Función de prueba utilizada en el código
def f_xy_4(var):
    global eval_f
    eval_f += 1
    f = (var[0] + 2 * var[1] - 7)**2 + (2 * var[0] + var[1] - 5)**2
    return f

# Ejecución de prueba
# max_pend_newton(f_xy_4, [3, 4], 0.00001)
```

-----

## 6\. Método de la Sección Dorada (Optimización 1D)

Implementación del método de la **Sección Dorada** para encontrar el mínimo de una función de una sola variable dentro de un intervalo cerrado.

```python
# -*- coding: utf-8 -*-
# Método de la Sección Dorada (Golden Section Search)

from math import *
from numpy import *
from sympy import *
from pandas import *
import time

# Solicitud de datos al usuario
while True:
    try:
        a = float(input("Ingresa el limite inferior del intervalo:\t"))
        b = float(input("Ingresa el limite superios del intervalo:\t"))
        gi = sympify(input("Ingresa la tolerancia:\t"))
        fx = sympify(input("Ingresa la función:\t"))
        break
    except:
        print("Ingresa de manera correcta los datos por favor")

L = b - a
tau = (-1 + pow(5, 1 / 2)) / 2
x1 = b - tau * L
x2 = a + tau * L

# Listas para almacenar resultados
LL = []
fxi = [fx.subs(x, x1)]
fx2i = [fx.subs(x, x2)]
LL.append(L)
xi = [x1]
x2i = [x2]

# Algoritmo de la Sección Dorada
while L >= gi:
    inicio = time.time()
    
    # Condición de descarte del subintervalo
    if fx.subs(x, x1) < fx.subs(x, x2):
        b = x2
        x2 = x1
        L = b - a
        x1 = b - tau * L
    else:
        a = x1
        x1 = x2
        L = b - a
        x2 = a + tau * L
        
    LL.append(L)
    fxi.append(fx.subs(x, x1))
    fx2i.append(fx.subs(x, x2))
    xi.append(x1)
    x2i.append(x2)
    fin = time.time()

# Creación de la tabla (DataFrame)
it = []
d = 0
for i in LL:
    d += 1
    it.append(d)

df = DataFrame()
df["Iteración"] = it
df["x1"] = xi
df["x2"] = x2i
df["f(x1)"] = fxi
df["f(x2)"] = fx2i
df["Error"] = LL

# Resultados finales
rl = xi[-1]
rl2 = x2i[-1]
# rl3 = fxi[-1]
# rl4 = fxi[-1] # rl4 es redundante, debe ser fx2i[-1]
# rrrr = min(rl3, rl4)

print("El punto optimo se encuentre en el intervalo ({},{})".format(rl, rl2))
print("La función evaluada en el punto óptimo es:\t{}".format(fx.subs(x, rl)))
print("Tiempo de ejecucion:\t {} segundos".format((fin - inicio)))
# df # Esto imprimiría el DataFrame en un entorno interactivo
```
