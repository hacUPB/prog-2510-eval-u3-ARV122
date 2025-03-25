# Control de inventario en una tienda

# Stock Tienda 
inventario = 50

while True:
    print("\nStock disponible: {inventario}")
    cantidad = int(input("¿Cuántos productos quieres comprar? "))
    
    if cantidad > inventario:
        print("No hay suficientes productos en el inventario") # En el papel solo llegue hasta esta parte 

# con ayuda de la inteligencia esto seria la continuidad del codigo 

    elif cantidad == 0:
        print("Has salido del sistema.")
        break  # Termina el bucle si el usuario ingresa 0

    else:
        inventario -= cantidad
        print(f"Compra realizada. Stock restante: {inventario}")

    # Si el inventario llega a 0, termina el programa
    if inventario == 0:
        print("Inventario agotado.")
        break










    