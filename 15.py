lista = []

for i in range(3):
    numero = int(input("Ingresa un número: "))
    lista.append(numero)
    
    lista.sort(reverse=True)
print("El número mayor es: ", lista[0])

