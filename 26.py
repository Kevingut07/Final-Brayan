inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20,
}

producto = input("Ingrese el nombre del producto que vendio: ")
cantidad = int(input("Ingrese la cantidad vendida: "))  

if producto in inventario:
    if cantidad <= inventario[producto]:
        inventario[producto] -= cantidad
        print("Venta realizada. Stock restante de " , producto, ": ", inventario[producto])
    else:
        print("No hay suficiente stock para completar la venta.")