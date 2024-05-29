# if statement = un bloque de codigo que se ejecuta solo si la condicion es verdadera

age = int(input('Cuantos años tienes?: '))

if age == 100:
    print('Eres un mito!')
elif age >= 18:
    print('Eres un adulto!')
elif age < 0:
    print('No has nacido!')
else:
    print('Eres un joven!')