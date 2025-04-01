# Verificar contraseña
# Pide al usuario que ingrese una contraseña.
# Si es correcta, imprimes "Acceso concedido", de lo contrario "Acceso denegado".
# Usa `if-else`

contraseña_correcta = "Programacion20153"

contraseña_ingresada = input("Ingrese la contraseña: ")

if contraseña_ingresada == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")

#Clasificar calificaciones**
#Pide al usuario una nota (0 a 5).
#Usa `if-elif-else` para clasificar (por ejemplo, 0-2 "Baja", 3-4 "Media", 5 "Alta").

nota = float(input("Ingrese una calificación (0 a 5): "))

if 0 <= nota <= 2:
    print("Clasificación: Baja")
elif 3 <= nota <= 4:
    print("Clasificación: Media")
elif nota == 5:
    print("Clasificación: Alta")
else:
    print("Error: La calificación debe estar entre 0 y 5.")

#Operación aritmética**
#Pide al usuario dos números y una opción: `+`, , , `/`.
#Utiliza `match-case` o `if-elif-else` para realizar la operación y mostrar el resultado.

# Solicitar números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Solicitar la operación
operacion = input("Seleccione la operación (+, -, *, /): ")

# Evaluar la operación con if-elif-else
if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida. Intente de nuevo.")
