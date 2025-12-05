notas = []

conteo = 0

for i in range(5):
    nota = float(input("Ingresa una nota: "))
    notas.append(nota)
    
for nota in notas:
    if nota >= 3.0: 
        conteo += 1
        
print("Número de notas mayores o iguales a 3.0: ", conteo)
    
