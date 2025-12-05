texto = input("Ingresa un texto: ")

conteo = {}

for letra in texto:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1
        
print("conteo de letras:", conteo)
