def suma_columnas(nombre_archivo):
    suma_col = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            numeros = list(map(int, linea.split()))
            if len(suma_col) < len(numeros):
                suma_col.extend([0] * (len(numeros) - len(suma_col)))
            for i in range(len(numeros)):
                suma_col[i] += numeros[i]
    return suma_col

print(suma_columnas('datos1.txt')) #esto es solo una prueba
