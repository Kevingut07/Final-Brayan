texto = input("Ingrese un texto: ")

vocales = "aeiou"

contador = 0

for letra in texto.lower():
    if letra in vocales:
        contador += 1
        
print("Número de vocales en el texto: ", contador)