nombres = []

while nombre != "fin":
    nombre = input("Ingrese un nombre (o 'salir' para terminar): ")
    nombres.append(nombre)
    if nombre == "fin":
        break
    
print(nombres)