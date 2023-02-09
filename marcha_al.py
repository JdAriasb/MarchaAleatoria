import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

def Marcha(n,N):
    """
    Toma un número n de pasos para generar una marcha aleatoria
    y un número N de veces que vamos a repetir las marcha
    
    Regresa una lista de las sumas de las marchas aleatorias.
    """
    X =rd.rand(N,n) # Lista en la que se guardarán los resultados de las marchas aleatorias.

    ii = X<p
    X[ii] = 1 
    X[~ii] = -1
    Mar = np.zeros(N)
    
    Mar = np.sum(X,axis=1)
    return Mar

def ProbTCL(n,s):
    """
    Toma un número de n pasos a realizar en la marcha aleatoria y un valor s para la suma total.

    Regresa la distribució de probabilidad esperada según el teorema central de límite.
    """
    av = n*(1*p + (1-p)*(-1)) # Valor medio teórico por medio del teorema central de límite.
    var = n*(1*p + 1*(1-p)) # Varianza teórica por medio del teorema central de límite.
    
    return (1/(np.sqrt(2*np.pi*var)))*np.exp((-(s-av)**2)/(2*var))


n = int(input("Introduzca número de pasos que dará la marcha aleatoria: ")) # Número de pasos aleatorios.
N = 10000 # Número de veces que se repetirá sa marcha aleatoria.
p = 0.5 # Probabilidad de que se de un paso a la derecha. (+1)
tau = 1 # Tiempo que transcurre para que se de un paso en segundos.

r = Marcha(n,N)


s = np.linspace(-100,100,1000) # Lista de valores de suma para graficar la densidad de probabilidad teórica.

#-----------------------Gráfica-----------------------------------
plt.figure()
plt.hist(r,bins=20, density=True, label="Histograma")
plt.plot(s, ProbTCL(n,s),label="Teorema central de límite",c="red")
plt.legend()
plt.grid()
plt.ylabel("Probabilidad p(x)")
plt.xlabel("Posición final en x [m]")
plt.title("Posición final luego de {} pasos.".format(n))
plt.savefig("Histograma.png")
#--------------------------------------------------------

ns = np.arange(1,1000,10)                         # Lista de diferentes valores de n
avs = np.zeros(len(ns)) 
avs2 = np.zeros(len(ns))
for i in range(len(ns)):
    Mi = Marcha(ns[i],N)
    avs[i] = np.average(Mi)                       # Se agregan los valores medios de las marchas aleatorias a una lista
    avs2[i] = np.average(Mi**2)                   # Se agregan los valores medios de las marchas aleatorias al cuadrado a una lista
r2 = avs2/ns                                      # A cada valor medio de las marchas al cuadrado se le divide el número de pasos que dió y los guarda en una lista.
print ("La varianza de los valores calculados para Δpi² es: {}".format(np.average(r2**2)-np.average(r2)**2))       # Imprime la varianza de la lista r2. Si el resultado de la varianza es un número cercano a cero, podemos decir que los valores medios de las marchas aleatorias al cuadrado son proporcionales al número de pasos.
avr2 =  np.average(r2)                            # valor medio de los valores calculados en r2.
D = 0.5 * avr2/tau                                # Constante de difusión calculada numéricamente.
print("El valor calculado para la constante de difusión es: {}".format(D))                                          # Imprime la constante de difusión.
