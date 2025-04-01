#**Menú Repetitivo**

# Crea un menú de opciones (por ejemplo, 1: "Sumar", 2: "Restar", 3: "Salir").
# Utiliza `while True:` para **mantener** el menú **hasta** que el usuario elija "Salir".
# Emplea `match-case` (o `if-elif-else` si no tienes Python 3.10+) para gestionar cada opción.

# Pregunta de Control**

#¿Cómo harías para terminar el bucle cuando el usuario elija "Salir"?
#¿En qué momento leerías la opción de usuario de nuevo para que el menú aparezca repetidamente?

while True:
    print("\n--- Menú de Operaciones ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado de la suma: {a + b}")

        case "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado de la resta: {a - b}")

        case "3":
            print("Saliendo del programa...")
            break  

        case _:
            print("Opción no válida, intente de nuevo.")

#Lo que Usamos para frenar el bucle cuando el usuario quiera salir es usando break dentro de case "3"