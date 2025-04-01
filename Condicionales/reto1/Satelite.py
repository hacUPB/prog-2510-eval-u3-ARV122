#Escribe un programa llamado `satelite.py` que simule la desintegración orbital de un satélite debido a la resistencia atmosférica. A medida que un satélite orbita la Tierra, pierde gradualmente altitud debido a las fuerzas de arrastre, las cuales aumentan a medida que el satélite se acerca a la Tierra.

#Descripción**:
# El satélite comienza a una altitud inicial específica y orbita la Tierra en una trayectoria circular.
# La fuerza de arrastre que actúa sobre el satélite aumenta a medida que desciende, lo que provoca una pérdida de altitud más rápida con el tiempo.
# El programa debe simular el descenso del satélite hasta que se estabilice en una órbita baja o reingrese en la atmósfera terrestre.

#Datos de entrada**:

#Altitud inicial**: La altitud inicial del satélite (en kilómetros).
#Coeficiente de arrastre**: Factor que determina la rapidez con la que el satélite pierde altitud. Este valor aumenta a medida que disminuye la altitud del satélite.
#Altitud mínima de seguridad**: Altitud por debajo de la cual se considera que el satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.
#Simulación de desintegración orbital**:- Solicita al usuario que ingrese la altitud inicial del satélite (en kilómetros).
# Solicita al usuario que ingrese el coeficiente de arrastre inicial (un valor decimal pequeño, como 0.01).
# Solicita al usuario que ingrese la altitud mínima de seguridad (en kilómetros).
#Proceso**:
#Utiliza un bucle para simular cada órbita (considera un bucle como una órbita alrededor de la Tierra).
#Para cada órbita:
# Calcula la pérdida de altitud debido al arrastre: `altitud_perdida = coeficiente_arrastre * altitud_actual`.
# Resta la pérdida de altitud a la altitud actual.
# Aumenta ligeramente el coeficiente de arrastre (por ejemplo, `coeficiente_arrastre += 0.0001`) para simular un aumento de la resistencia a medida que disminuye la altitud.
# Detén el bucle si el satélite alcanza la altitud mínima de seguridad o si se estabiliza (es decir, la pérdida de altitud se vuelve muy pequeña).
#3. **Salida**:
#Si el satélite se estabiliza en órbita (la pérdida de altitud es muy pequeña), muestra la altitud final y el número de órbitas completadas.
# Si el satélite reingresa en la atmósfera terrestre, muestra un mensaje indicando el reingreso y el número total de órbitas completadas

# Simulador de desintegración orbital de un satélite

altitud = float(input("Ingrese la altitud inicial del satélite (km): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (ejemplo: 0.01): "))
altitud_minima = float(input("Ingrese la altitud mínima de seguridad (km): "))

orbita = 0  

while altitud > altitud_minima:
    altitud_perdida = coeficiente_arrastre * altitud
    altitud -= altitud_perdida
    coeficiente_arrastre += 0.0001  
    orbita += 1
    
    
    if altitud_perdida < 0.01:
        print(f"El satélite se ha estabilizado en una órbita baja a {altitud:.2f} km después de {orbita} órbitas.")
        break
else:
    print(f"El satélite ha reingresado en la atmósfera después de {orbita} órbitas y se ha desintegrado.")
