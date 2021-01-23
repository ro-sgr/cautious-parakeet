import numpy as np

# Parámetros constantes:
k = 1.
A = 1.
B = 1.
R = 1.
I = 1.

def calcular_thetadpt(ang, vel):
    ac_ang = (- k * ang )/I - (((A*B)**2)* ((np.cos(ang)) ** 2) * vel) / R # Cálculo de la aceleración angular según la ecuación diferencial
    return ac_ang

TIEMPO = []
THETA = []

def f(tiempo):
    # Valores iniciales
    theta = 1.
    thetapt = 0.
    dt = 0.01 # Paso
    for i in np.arange(0,tiempo,dt):
        TIEMPO.append(i) # Se adjunta el segundo a una lista
        thetadpt = calcular_thetadpt(theta, thetapt) # Se calcula la aceleración angular según las variables
        thetapt += thetadpt * dt # Como thetapt = d/dt (thetapt), theta_f = thetapt_i + thetadpt * dt, aprox
        theta += thetapt * dt # Como thetapt = d/dt (theta), theta_f = thetapt_i + thetadpt * dt, aprox
        THETA.append(theta)

tiempo = float(input("Tiempo: "))
f(tiempo)
print(THETA)
