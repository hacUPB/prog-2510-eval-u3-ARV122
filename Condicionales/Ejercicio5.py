#El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, 
# con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida al usuario su edad 
# y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario 
# no ingrese valores menores a cero. Clasificación etaria de la población colombiana:

# Primera Infancia (0-5 años)
# Infancia (6 - 11 años)
# Adolescencia (12 - 18 años)
# Juventud (14 - 26 años)
# Adultez (27- 59 años)
# Persona Mayor (60 años o más) envejecimiento y vejez

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Error: La edad no puede ser un número negativo.")

else:
    if 0 <= edad <= 5:
        etapa = "Primera Infancia"
    elif 6 <= edad <= 11:
        etapa = "Infancia"
    elif 12 <= edad <= 18:
        etapa = "Adolescencia"
    elif 14 <= edad <= 26:
        etapa = "Juventud"
    elif 27 <= edad <= 59:
        etapa = "Adultez"
    else:  # edad >= 60
        etapa = "Persona Mayor (Envejecimiento y Vejez)"

    print(f"Según su edad ({edad} años), usted está en la etapa de: {etapa}.")
