
with open("C:\\Users\\Angel Poveda\\Desktop\\test.txt") as file:    # usando with open el archivo se cierra luego de abrirse
    print(file.read())

print(file.closed)