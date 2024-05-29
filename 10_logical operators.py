# logical operators (and,or) = usados para revisar si uno o más declaraciones condicionales son verdaderas

temp = float(input('Cual es la temperatura afuera?: '))

if temp >= 0 and temp <= 30:
    print('la temperatura esta normal el día de hoy!')
    print('Sal a jugar!!')
elif temp < 0 or temp > 30:
    print('la temperatura esta pesima hoy!')
    print('QUEDATE EN CASA!!!')