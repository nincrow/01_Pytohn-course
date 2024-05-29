# while loops = una declaracion que ejecutara un bloque de codigo, siempre y cuando la condicion se mantenga verdadera

name = ''

while len(name) == 0:
    name = input('Introduzca su nombre: ')

print('Hola '+name)