# dictionary = Una coleccion cambiante, desordenada de pares de valores:claves. Rapido porque estos usan "picadillo", permitiendonos el acceso rapido a los valores

from multiprocessing.sharedctypes import Value


capitals = {'USA':'Washignton DC' ,
            'India':'NeW Dheli' ,
            'China':'Beijing' ,
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()

#print(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)