def es_mutante(adn):
    # Variables para el tamaño de la matriz y la cantidad de secuencias encontradas
    n = len(adn)
    secuencias_encontradas = 0

    # Función auxiliar para verificar una secuencia de cuatro letras
    def tiene_secuencia(x, y, dx, dy):
        base = adn[x][y]
        for i in range(1, 4):
            if not (0 <= x + dx * i < n and 0 <= y + dy * i < n) or adn[x + dx * i][y + dy * i] != base:
                return False
        return True

    # Revisar todas las posiciones de la matriz
    for i in range(n):
        for j in range(n):
            # Revisar si hay una secuencia de 4 en dirección:
            # - Horizontal (dx=0, dy=1)
            # - Vertical (dx=1, dy=0)
            # - Diagonal hacia la derecha (dx=1, dy=1)
            # - Diagonal hacia la izquierda (dx=1, dy=-1)
            if (j + 3 < n and tiene_secuencia(i, j, 0, 1)) or \
               (i + 3 < n and tiene_secuencia(i, j, 1, 0)) or \
               (i + 3 < n and j + 3 < n and tiene_secuencia(i, j, 1, 1)) or \
               (i + 3 < n and j - 3 >= 0 and tiene_secuencia(i, j, 1, -1)):
                secuencias_encontradas += 1

                # Si encontramos más de una secuencia, es mutante
                if secuencias_encontradas > 1:
                    return True

    return False

adn_no_mutante = [
    "ATGCGA",
    "CAGTGC",
    "TTATTT",
    "AGACGG",
    "GCGTCA",
    "TCACTG"
]

adn_mutante = [
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
]

print(es_mutante(adn_no_mutante))  # Salida: False
print(es_mutante(adn_mutante))     # Salida: True
