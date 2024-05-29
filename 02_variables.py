# variable = a container for a value. Behaves as the value tht it contains

# STRING DATA TYPE
first_name = 'Angel'
last_name = 'Poveda'
full_name = first_name + ' '+ last_name

print('Hello '+full_name)

#con la funcion: print(type(variable)), se puede ver el tipo de dato de una variable
print(type(first_name))


# INT (INTEGER, enteros) DATA TYPE
age = 21
age += 1
#shortcut age += 1

#las variables int no pueden mezclarse con los string; print('Mi edad es de: '+age)
#para que funcione la variable int debe tener la funcion str antes; print('Mi edad es de: '+str (age))
print('Mi edad es de: '+str (age))
print(type(age))


#FLOAT (FLOATING POINT NUMBER, decimal) DATA TYPE

altura = 250.3
print("Tu altura es: "+str(altura)+'cm')
print(type(altura))
#igual que las variables int para imprimir los float con texto se le agrega la funcion str


#BOOLEAN (Verdadero o Falso) DATA TYPE

humano = False
print('Eres un humano: '+str(humano))
print(type(humano))