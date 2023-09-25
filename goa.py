from random import *
from math import *

# ========= PARAMETROS =========
MAX_ITER = 20  # Numero maximo de iteraciones
DIM = 10  # Tamano de solucion
N = 20  # Tamano de poblacion

M = 2.5  # Peso en Kg del Gannet
VEL = 1.5  # Velocidad en el agua en m/s del Gannet
BETA = 1.5
C = 0.2  # Determina si se ejejuta movimiento levy o ajustes de trayectoria
FACTOR_FASE = (
    0.5  # Determina que fase exploracion o explotacion usa el algoritmo en la iteracion
)

UB = 1
LB = 0

MU = uniform(0, 1)
V_SIGMA = uniform(0, 1)


# ========= FUNCIONES =========
def v(x):
    if x > pi:
        return (1 / pi) * x - 1
    return -(1 / pi) * x + 1


def levy():
    valor = 0.01
    return valor


# ========= ALGORITMO =========

x = iniciar_poblacion_random(N, DIM)

mx = x.copy()  # Crear matriz de memoria

# Busca mejor solucion

iter_actual = 0
while iter_actual < MAX_ITER:
    rand = uniform(0, 1)

    # Calculos constantes por iteracion
    t = 1 - (iter_actual / MAX_ITER)

    individuo_mejor = obtener_mejor_individuo(mx)
    individuo_random = obtener_individuo_random(mx)
    individuo_promedio = obtener_promedio_individuos(mx)

    # ========= Exploracion =========
    if rand > 0.5:
        # Recorre la matriz de memoria
        for i in range(N):
            q = uniform(0, 1)
            if q >= 0.5:
                for j in range(DIM):
                    r2 = uniform(0, 1)
                    r4 = uniform(0, 1)

                    a = 2 * cos(2 * pi * r2) * t
                    a_may = (2 * r4 - 1) * a

                    u1 = uniform(-a, a)
                    u2 = a_may * (x[i][j] - individuo_random[j])

                    # Ecuacion 7a
                    mx[i][j] = x[i][j] + u1 + u2
            else:
                for j in range(DIM):
                    r3 = uniform(0, 1)
                    r5 = uniform(0, 1)

                    b = 2 * v(2 * pi * r3) * t
                    b_may = (2 * r5 - 1) * b

                    v1 = uniform(-b, b)
                    v2 = b_may * (x[i][j] - individuo_promedio[j])
                    # Ecuacion 7b
                    mx[i][j] = x[i][j] + v1 + v2

    # ========= Explotacion =========
    else:
        # Recorre la matriz de memoria
        for i in range(N):
            t2 = 1 + (iter_actual / MAX_ITER)
            r6 = uniform(0, 1)
            l = 0.2 + (2 - 0.2) * r6
            r = (M * VEL**2) / l
            capturability = 1 / (r * t2)
            # Caso ajustes exitosos
            if capturability >= C:
                for j in range(DIM):
                    delta = capturability * abs(x[i][j] - individuo_mejor[j])
                    # Ecuacion 17a
                    mx[i][j] = t * delta * (x[i][j] - individuo_mejor[j]) + x[i][j]
            # Caso movimiento Levy
            else:
                for j in range(DIM):
                    p = levy()
                    # Ecuacion 17b
                    mx[i][j] = (
                        individuo_mejor[j] - (x[i][j] - individuo_mejor[j]) * p * t
                    )
    for i in range(n):
        # Calculate fitnes of Mxi
        if fitnessMx > fintensX:
            xi = Mxi
    iter_actual += 1
