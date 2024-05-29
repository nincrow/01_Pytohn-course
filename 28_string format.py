# str.format() =    optional method that gives users more control when displaying output

animal = 'cow'
item = 'moon'

print('The '+animal+' jumped over the '+item)
print('The {} jumped over the {}'.format(animal,item))
print('The {0} jumped over the {1}'.format(animal,item)) #positional argumnet
print('The {item} jumped over the {animal}'.format(animal='cow',item='moon')) #keyword argument

text = 'The {} jumped over the {}'
print(text.format(animal,item))



#####################################


name = 'Angel'

print('Hello my name is {}'.format(name))
print('Hello my name is {:10}. Nice to meet you'.format(name))
print('Hello my name is {:<10}. Nice to meet you'.format(name))
print('Hello my name is {:>10}. Nice to meet you'.format(name))
print('Hello my name is {:^10}. Nice to meet you'.format(name))



####################################

pi = 3.14159
number = 1000

print('The number pi is {:.2f}'.format(pi))
print('The number is {:,}'.format(number))
print('The number is {:b}'.format(number))
print('The number is {:0}'.format(number))
print('The number is {:x}'.format(number))
print('The number is {:e}'.format(number))