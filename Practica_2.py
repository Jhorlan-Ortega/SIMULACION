import random as ran
import numpy as np
import math

# Distribución de probabilidad de ventas
def ventas():
    r = ran.random()
    if r <= 0.3:
        return 100
    elif r <= 0.5:
        return 150
    elif r <= 0.8:
        return 200
    elif r <= 0.95:
        return 250
    else:
        return 300

# Simulación de ganancias
def simular_ganancias(encargo, iteraciones=10000):
    ganancias = []
    for _ in range(iteraciones):
        # Generar costo por unidad con transformada inversa
        costo_unitario = ran.uniform(1.5, 2.0)
        costo_total = encargo * costo_unitario

        # Obtener demanda simulada
        demanda = ventas()

        # Calcular ventas y reembolsos
        ventas_totales = min(demanda, encargo) * 4.5
        sobrantes = max(encargo - demanda, 0)
        reembolso = sobrantes * 0.75

        # Calcular utilidad
        utilidad = ventas_totales - costo_total + reembolso
        ganancias.append(utilidad)

    return np.mean(ganancias), np.std(ganancias)

# Calcular número de simulaciones necesarias
def calcular_num_simulaciones(desviacion, precision=10, confianza=0.95):
    z = 1.96  # Para 95% de confianza
    return math.ceil((z * desviacion / precision) ** 2)

# Intervalo de confianza
def calcular_intervalo_confianza(media, desviacion, n, confianza=0.95):
    z = 1.96  # Para 95% de confianza
    margen_error = z * desviacion / math.sqrt(n)
    return media - margen_error, media + margen_error

# Determinar número óptimo de almanaques
def encontrar_optimo():
    resultados = {}
    for encargo in range(100, 301, 50):  # Iterar desde 100 a 300 almanaques en pasos de 50
        media, desviacion = simular_ganancias(encargo)
        resultados[encargo] = (media, desviacion)
    optimo = max(resultados, key=lambda x: resultados[x][0])
    return optimo, resultados

# Ejecución principal
optimo, resultados = encontrar_optimo()
media_optimo, desv_optimo = resultados[optimo]

# Calcular simulaciones necesarias
num_simulaciones = calcular_num_simulaciones(desv_optimo)

# Repetir simulaciones con el número óptimo de simulaciones
media_final, desv_final = simular_ganancias(optimo, num_simulaciones)

# Calcular intervalo de confianza
ic_inf, ic_sup = calcular_intervalo_confianza(media_final, desv_final, num_simulaciones)

# Imprimir resultados
print(f"Número óptimo de almanaques: {optimo}")
print(f"Ganancia esperada: ${media_final:.2f}")
print(f"Desviación estándar: ${desv_final:.2f}")
print(f"Intervalo de confianza al 95%: (${ic_inf:.2f}, ${ic_sup:.2f})")
print(f"Simulaciones requeridas: {num_simulaciones}")