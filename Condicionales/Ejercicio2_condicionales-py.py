#Resuelve el siguiente problema usando el condicional simple.
#Un almacén cobra $9 000 por costos de envío, 
#pero ofrece el envío a domicilio gratis para compras superiores a $100 000. 
#En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra 
#y calcule el valor total a pagar.

valor_compra = float(input("Ingrese el valor de la compra: "))
costo_envio = 9000

if valor_compra > 100000:
    costo_envio = 0

total_a_pagar = valor_compra + costo_envio

print(f"Valor de la compra: ${valor_compra:,.0f}")
print(f"Costo de envío: ${costo_envio:,.0f}")
print(f"Total a pagar: ${total_a_pagar:,.0f}")
