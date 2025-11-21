#Declarar variables
nombre = ""
precio = 0
cantidad = 0
costo_total = 0

#Solicitar datos al usuario
nombre = input("Ingresar nombre del producto: ")

#Ciclo el cual valida que el dato sea correcto, mientras el dato no sea correcto el bloque se repite y sigue solicitando el dato
while True:
    try:
        precio = float(input("Ingresar el precio del producto: "))
        if precio > 0: #Validar que el precio sea un número positivo
            break #Si se cumple, sale del bucle dandole continuidad al código
        else: 
            print("El precio debe ser un número positivo")
    except ValueError:
        print("Escribir un valor válido para este campo")

#Ciclo el cual valida que el dato sea correcto, mientras el dato no sea correcto el bloque se repite y sigue solicitando el dato
while True:
    try:
        cantidad = int(input("Ingresar la cantidad de productos: "))
        if cantidad > 0: #Validar que cantidad sea un número positivo
            break #Si se cumple, sale del bucle dandole continuidad al código
        else: 
            print("La cantidad debe ser un número positivo")        
    except ValueError:
        print("Escribir un valor válido para este campo")

#Calcular el costo total
costo_total = precio*cantidad

#Imprimir resultado
print(f"Nombre producto: {nombre} \nPrecio unitario: {precio} \nCantidad: {cantidad} \nCosto total: {costo_total}")

#