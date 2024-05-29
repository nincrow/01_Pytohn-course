# slicing = crea un substring esxtrayendolo de otro string
#           indexing[] or slice()
#           [start:stop:step]   para start comineza en 0, stop comienza en 1

from ast import Slice


name ='Angel Poveda'

first_name = name[:5]
last_name = name[6:]
funky_name = name[::2]
reversed_name =name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = 'http://google.com'
website2 = 'http://wikipedia.com'

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])