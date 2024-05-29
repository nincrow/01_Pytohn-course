# tuples = coleccion que esta ordenada y no se puede cambiar, usada para agrupar datos relacionados

student = ('Angel',22,'male')

print(student.count('Angel'))
print(student.index('male'))

for x in student:
    print(x)

if 'Angel' in student:
    print('Angel is here!')