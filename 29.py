dic = {
    "Kevin": 23,
    "Michell": 30,
    "Juan": 25,
    "Ana": 28
}

ordenados = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

print("El siguiente jugador es el campeon, felicidades: ", list(ordenados.items())[0])