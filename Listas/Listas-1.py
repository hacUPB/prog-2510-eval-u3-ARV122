'''
#Ejercicio
1. solicitar al usuario una frase de al menos 30 palabras 
2. contar cuantas palabras hay en una frase
3. contar cuantos caracteres, incluyendo espacios en blanco hay en el texto 
4. contar los caracteres sin espacios en blanco

regla resto de semestre 
No se permite el uso de list comprehension, ni de funciones avanzadas 
'''

Frase = "La lectura es más fácil, también, en la nueva vista de lectura. Puede contraer partes del documento y centrarse en el texto que desee. Si necesita detener la lectura antes de llegar al final, Word le recordará dónde dejó la lectura, incluso en otros dispositivos."
caracteres_con_espacio = len(Frase)
print(caracteres_con_espacio)
lista_palabras = Frase.split() # es lo mimso que split("")
print(lista_palabras)
num_palabras = len(lista_palabras)
print(f"palabras en la frase: {num_palabras}")
blancos = Frase.count(" ")
print(f"espacios en blanco: {blancos}")
caracteres_sin_espacio = caracteres_con_espacio - blancos
print(f"Total caracteres sin espacio: {caracteres_sin_espacio}")
letras_a = Frase.lower().count('a')
letras_e = Frase.lower().count('e')
print(f"La letra que mas se repite {letras_a} veces y la e {letras_e} veces.")
