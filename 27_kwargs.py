# **kwargs =    parameter that willl pack all argumnets into a dictionary
#               useful so that a function can accept a varying amount of keyword argumnets

def hello(**kwargs):
    #print('Hello '+ kwargs['first'] + ' ' + kwargs['last'])
    print('Hello',end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')

hello(first='Angel',middle='Moises',last='Poveda')