import scipy.stats as stats
import math

# Datos del problema
mu = 70000        # Media poblacional
sigma = 2500      # Desviación estándar poblacional
n = 25            # Tamaño de la muestra
x_barra = 69100   # Media de la muestra observada
limite_seguridad = 65000
nivel_significancia = 0.05

print("--- RESULTADOS DEL ANÁLISIS ---")

# 1. Probabilidad de falla (X < 65000)
# Usamos la función de distribución acumulada (cdf)
prob_falla = stats.norm.cdf(limite_seguridad, mu, sigma)
print(f"1. Probabilidad de que una viga falle: {prob_falla:.4%}")

# 2. Prueba de Hipótesis
# H0: mu = 70000 (El proceso está bien)
# H1: mu < 70000 (La resistencia ha disminuido)
error_estandar = sigma / math.sqrt(n)
z_stat = (x_barra - mu) / error_estandar
p_valor = stats.norm.cdf(z_stat) # Área a la izquierda del estadístico

print(f"2. Prueba de Hipótesis:")
print(f"   - Estadístico Z: {z_stat:.4f}")
print(f"   - P-valor: {p_valor:.4f}")

if p_valor < nivel_significancia:
    print("   - RESULTADO: Rechazamos H0. Hay evidencia para detener la producción.")
else:
    print("   - RESULTADO: No hay evidencia suficiente para detener la producción.")

# 3. Garantía de Calidad (Percentil 1)
# Usamos la función punto-porcentual (ppf) que es la inversa de la cdf
resistencia_minima = stats.norm.ppf(0.01, mu, sigma)
print(f"3. Resistencia del catálogo (Percentil 1): {resistencia_minima:.2f} psi")