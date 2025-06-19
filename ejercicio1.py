# **Enunciado:**  
# Un agricultor necesita monitorear la temperatura de su invernadero para asegurar el crecimiento óptimo de sus plantas. 
# Debes ayudarle a identificar si las temperaturas registradas están dentro del rango adecuado y alertar si alguna es peligrosa.

# **Indicaciones paso a paso:**
# 1. Solicita al usuario que ingrese 5 temperaturas.
# 2. Guarda las temperaturas en una lista.
# 3. Calcula el promedio y la temperatura máxima.
# 4. Verifica si todas las temperaturas están entre 15°C y 30°C.
# 5. Si alguna temperatura está fuera de 10°C–35°C, muestra una advertencia.

# **Puntos asignados:** 25 pts

# **Criterios evaluados:**
# - Uso correcto de lista y cálculos (10 pts)
# - Evaluación de condiciones lógicas (10 pts)
# - Orden y claridad del código (5 pts)

temperaturas = []
for i in range (5):
    ingresar_temperatura = int(input("Ingresa 5 temperaturas: "))
    temperaturas.append(ingresar_temperatura)

promedio = sum(temperaturas)/len(temperaturas)
temperatura_maxima = max(temperaturas)
if ingresar_temperatura >= 15 and ingresar_temperatura <= 30:
    print(temperatura_maxima)
    print(promedio)
    print("todas las temperaturas estan en un rango de 15 y 30 grados")
else:
    ingresar_temperatura < 15 and ingresar_temperatura > 30
    print("Advertencia, hay temperaturas fuera del rango")
    