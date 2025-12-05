paises = {
    "colombia": "Bogotá",
    "méxico": "Ciudad de México",
    "argentina": "Buenos Aires",
    "perú": "Lima",
    "chile": "Santiago"
}

pais = input("Ingrese el nombre de un país: ")

if pais in paises:
    print("La capital de", pais, "es", paises[pais])
else:
    print("No esta registrado.")