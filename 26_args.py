# *args =   parameter that will pack all arguments into a tuple
#           useeful so that a function can accept a varying amount of argumnets

def add(*thing):
    sum = 0
    thing = list(thing)
    thing[0] = 0
    for i in thing:
        sum += i
    return sum

print(add(1,2,3,4,5))