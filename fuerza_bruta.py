# FUERZA BRUTA - PROBLEMA DE LA MOCHILA
n = 5
capacidad = 10

peso = [2, 5, 4, 3, 6]
ganancia = [25, 60, 50, 40, 90]

mejor_ganancia = 0
mejor_peso = 0
mejor_pedido = [False] * n

print("=================================")
print(" FUERZA BRUTA - DELIVERY ")
print("=================================")

for mascara in range(2 ** n):

    peso_total = 0
    ganancia_total = 0
    temp = mascara

    print()
    print("Combinacion", mascara)
    print("Pedidos incluidos:")

    for i in range(n):

        if temp % 2 == 1:
            print("Pedido", i + 1)

            peso_total += peso[i]
            ganancia_total += ganancia[i]

        temp = temp // 2

    print("Peso total:", peso_total)
    print("Ganancia total:", ganancia_total)

    if peso_total <= capacidad:

        print("Estado: VALIDA")

        if ganancia_total > mejor_ganancia:

            mejor_ganancia = ganancia_total
            mejor_peso = peso_total

            temp = mascara

            for i in range(n):

                if temp % 2 == 1:
                    mejor_pedido[i] = True
                else:
                    mejor_pedido[i] = False

                temp = temp // 2

            print("*** NUEVA MEJOR SOLUCION ***")

    else:

        print("Estado: EXCEDE CAPACIDAD")

print()
print("=================================")
print(" MEJOR SOLUCION ENCONTRADA ")
print("=================================")

print("Pedidos seleccionados:")

for i in range(n):
    if mejor_pedido[i]:
        print("Pedido", i + 1)

print("Peso total:", mejor_peso)
print("Ganancia maxima:", mejor_ganancia)