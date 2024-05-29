#   nested loops = El "bucle interno" terminara todas sus iteraciones antes de terminara una iteracion del "bucle externo"

rows = int(input('Cuantas filas?: '))
columns = int(input('Cuantas columnas?: '))
symbol = input('Coloca un simbolo a usar: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()