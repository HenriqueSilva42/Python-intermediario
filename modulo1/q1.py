def imprimir_intervalo(a, b):
    if a > b:
        print("Valores invalidos")
    else:
        def recursao(x):
            if x > b:
                return
            print(x, " ", end="")
            recursao(x + 1)
        recursao(a)
        print()

# Exemplos de uso para Q1
imprimir_intervalo(1, 10)  # 1 2 3 4 5 6 7 8 9 10
imprimir_intervalo(-5, 1)  # -5 -4 -3 -2 -1 0 1
imprimir_intervalo(5, -5)  # Valores invalidos
imprimir_intervalo(17, 20)  # 17 18 19 20
