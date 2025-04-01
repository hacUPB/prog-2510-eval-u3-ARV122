marcas_camisetas = ["Undergold","Clemont", "Monoic", "Pure"]

# Agregar un elemento al final de la lista
marcas_camisetas.append("Perspective")
print(marcas_camisetas)
# Insertar un elemento en una posición específica
marcas_camisetas.insert(3, "Saint theory")
print(marcas_camisetas)

# Extender la lista con otra lista
marcas_camisetas.extend(["Off white", "Breath"])
print(marcas_camisetas)

# remover un elemento de la lista 
marcas_camisetas.remove("Pure")
print(marcas_camisetas)

#numeros = [1, 2, 3, 4, 5]

# Eliminar un elemento por valor
#numeros.remove(3)

# Eliminar un elemento por índice y obtener su valor
#valor_eliminado = numeros.pop(1)

# Eliminar todos los elementos de la lista
#numeros.clear()

#print(numeros)
#print("Valor Eliminado:", valor_eliminado)

# Ordenar la lista alfabéticamente (ascendente)
marcas_camisetas.sort()
print(marcas_camisetas)

# Ordenar la lista alfabéticamente en orden descendente
marcas_camisetas.sort(reverse=True)
print(marcas_camisetas)

# Revertir el orden de la lista
marcas_camisetas.reverse()
print(marcas_camisetas)

# Contar la cantidad de veces que aparece un elemento
marcas_camisetas = marcas_camisetas.count("Monoic")
print(marcas_camisetas)