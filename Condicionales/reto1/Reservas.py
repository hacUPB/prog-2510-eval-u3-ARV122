#Entrega un archivo llamado reservas.py que resuelva la siguiente solicitud:

#Sistema de Reservas de Aerolíneas**

#Desarrolla un sistema sencillo de reservas de aerolíneas. Este programa permitirá al usuario ingresar su información personal y elegir un vuelo. El programa debe realizar lo siguiente:

#Información del usuario**:
# Solicita al usuario que ingrese su título (Sr. o Sra.), nombre y apellido.
# Muestra un saludo personalizado utilizando el nombre completo del usuario. Ejemplo: "Sr. Juan Pérez, ¡Bienvenido a FastFast Airlines!"
#Selección de vuelo**:
# Permite al usuario seleccionar un origen y destino entre las siguientes ciudades: Medellín, Bogotá, Cartagena. Puedes cambiar las ciudades de destino.
#Solicita al usuario que ingrese el día de la semana en el que desea viajar (por ejemplo, lunes) y el día del mes (un número entre 1 y 30).
#Calcula el precio del billete dependiendo de la distancia entre las ciudades y el día de la semana, utilizando las siguientes reglas:- Si la distancia entre las ciudades es inferior a 400 km:
# De lunes a jueves, el precio es de $79,900.
# De viernes a domingo, el precio es de $119,900.
# Si la distancia entre las ciudades es de 400 km o más:
# De lunes a jueves, el precio es de $156,900.
# De viernes a domingo, el precio es de $213,000.

#Distancias entre ciudades**:

# Medellín a Bogotá: 240 km.
# Medellín a Cartagena: 461 km.
# Bogotá a Cartagena: 657 km.
#Asignación de asiento**:
# Pregunta al usuario si prefiere un asiento en el pasillo, junto a la ventana, o si no tiene preferencia.
# Asigna el asiento según la preferencia:
#Pasillo: Asiento C.
# Ventana: Asiento A.- Sin preferencia: Asiento B.
# Selecciona aleatoriamente un número de asiento entre 1 y 29 utilizando random.randint(1, 29) y muestra el asiento asignado (por ejemplo, 20C).
#Salida**:
#Muestra el nombre completo del usuario, origen, destino, fecha de vuelo, precio del boleto y asiento asignado.

import random

titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a Vuelosinterrapidos!")

print("Ciudades disponibles: Medellín, Bogotá, Cartagena")
origen = input("Ingrese su ciudad de origen: ")
destino = input("Ingrese su ciudad de destino: ")

while origen == destino:
    print("El origen y destino no pueden ser la misma ciudad. Intente de nuevo.")
    destino = input("Ingrese su ciudad de destino: ")

distancias = {
    ("Medellín", "Bogotá"): 240,
    ("Bogotá", "Medellín"): 240,
    ("Medellín", "Cartagena"): 461,
    ("Cartagena", "Medellín"): 461,
    ("Bogotá", "Cartagena"): 657,
    ("Cartagena", "Bogotá"): 657
}

distancia = distancias.get((origen, destino), 0)

dia_semana = input("Ingrese el día de la semana en que desea viajar: ")
dia_mes = int(input("Ingrese el día del mes (1-30): "))

if distancia < 400:
    if dia_semana.lower() in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 79900
    else:
        precio = 119900
else:
    if dia_semana.lower() in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 156900
    else:
        precio = 213000

print("Preferencias de asiento: pasillo, ventana, sin preferencia")
preferencia_asiento = input("Ingrese su preferencia de asiento: ")

if preferencia_asiento.lower() == "pasillo":
    letra_asiento = "C"
elif preferencia_asiento.lower() == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

numero_asiento = random.randint(1, 29)
asiento_asignado = f"{numero_asiento}{letra_asiento}"

print("\nRESUMEN DE RESERVA")
print(f"Pasajero: {titulo} {nombre} {apellido}")
print(f"Origen: {origen}")
print(f"Destino: {destino}")
print(f"Fecha de vuelo: {dia_semana}, {dia_mes}")
print(f"Precio del billete: ${precio}")
print(f"Asiento asignado: {asiento_asignado}")
