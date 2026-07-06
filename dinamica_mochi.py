import time

def mochila_dinamica(pesos, ganancias, capacidad_maxima):
    n = len(pesos)

    dp = [[0] * (capacidad_maxima + 1) for _ in range(n + 1)]

    for f in range(1, n + 1):         
        peso_f     = pesos[f - 1]     
        ganancia_f = ganancias[f - 1]   

        for c in range(capacidad_maxima + 1):   
            opcion_sin = dp[f - 1][c]           

            if peso_f <= c:                     
                opcion_con = ganancia_f + dp[f - 1][c - peso_f]
                dp[f][c] = max(opcion_sin, opcion_con)
            else:                               
                dp[f][c] = opcion_sin

    seleccionados = []
    col_actual    = capacidad_maxima

    for fila in range(n, 0, -1):
        if dp[fila][col_actual] != dp[fila - 1][col_actual]:
            seleccionados.append(fila)                   
            col_actual -= pesos[fila - 1]                
        if col_actual <= 0:
            break

    seleccionados.reverse()

    ganancia_max = dp[n][capacidad_maxima]
    return ganancia_max, seleccionados, dp


def imprimir_tabla_dp(dp, n, capacidad_maxima):
    print("\n─ TABLA DE PROGRAMACIÓN DINÁMICA (dp[pedido][capacidad]) ─")
    cabecera = "     " + "".join(f" {c:4}" for c in range(capacidad_maxima + 1))
    print(cabecera)
    print("     " + "─" * ((capacidad_maxima + 1) * 5))
    for f in range(n + 1):
        etiqueta = f"  {f:2} │" if f > 0 else "   0 │"
        fila_str = "".join(f" {dp[f][c]:4}" for c in range(capacidad_maxima + 1))
        print(etiqueta + fila_str)


def analisis_empirico():
    import random

    print("\n" + "=" * 60)
    print("  ANÁLISIS EMPÍRICO — PROGRAMACIÓN DINÁMICA")
    print("=" * 60)
    print(f"{'n (pedidos)':>12} {'Capacidad':>10} {'Tiempo (ms)':>14} {'Ganancia máx':>14}")
    print("-" * 60)

    tamaños = [5, 10, 20, 50, 100, 200]
    for n in tamaños:
        random.seed(42)
        pesos_     = [random.randint(1, 20) for _ in range(n)]
        ganancias_ = [random.randint(10, 200) for _ in range(n)]
        capacidad_ = n * 5

        inicio      = time.perf_counter()
        ganancia, _, _ = mochila_dinamica(pesos_, ganancias_, capacidad_)
        fin         = time.perf_counter()
        tiempo_ms   = (fin - inicio) * 1000

        print(f"{n:>12} {capacidad_:>10} {tiempo_ms:>13.4f} {ganancia:>14}")

    print("=" * 60)


def main():
    n                = 5
    capacidad_maxima = 10

    pesos     = [2, 5, 4, 3, 6]
    ganancias = [25, 60, 50, 40, 90]

    inicio = time.perf_counter()
    ganancia_max, seleccionados, dp = mochila_dinamica(
        pesos, ganancias, capacidad_maxima
    )
    fin       = time.perf_counter()
    tiempo_us = (fin - inicio) * 1_000_000 

    imprimir_tabla_dp(dp, n, capacidad_maxima)

    peso_total    = sum(pesos[i - 1]     for i in seleccionados)
    ganancia_real = sum(ganancias[i - 1] for i in seleccionados)

    print("\n" + "=" * 45)
    print("  ALGORITMO: Programación Dinámica (Python)")
    print("=" * 45)
    print(f"  Número de pedidos disponibles : {n}")
    print(f"  Capacidad máxima              : {capacidad_maxima} kg")
    print(f"  Complejidad temporal          : O(n × W) = O({n} × {capacidad_maxima}) = O({n * capacidad_maxima})")
    print("-" * 45)
    print("  Pedidos seleccionados:")
    print(f"  {'Pedido':>8}  {'Peso':>6}  {'Ganancia':>10}")
    print(f"  {'──────':>8}  {'────':>6}  {'────────':>10}")
    for i in seleccionados:
        print(f"  Pedido {i:>2}   {pesos[i-1]:>4} kg   S/. {ganancias[i-1]:>6}")
    print("-" * 45)
    print(f"  Peso total usado              : {peso_total} / {capacidad_maxima} kg")
    print(f"  Ganancia máxima posible       : S/. {ganancia_max}")
    print(f"  Tiempo de ejecución           : {tiempo_us:.4f} µs")
    print("=" * 45)

    analisis_empirico()


if __name__ == "__main__":
    main()