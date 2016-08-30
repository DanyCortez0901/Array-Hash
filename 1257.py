def suma(lista):
    total = 0
    indice = 0
    indice2 = 0
    for x in lista:
        indice = 0
        for i in x:
            total += (indice2 + (ord(i)-65) + indice)
            indice += 1
        indice2 += 1
    return total


def hasharray():
    casos = input()
    for i in range(int(casos)):
        lineas = input()
        linea = []
        for j in range(int(lineas)):
            linea.append(input())
        print(suma(linea))
