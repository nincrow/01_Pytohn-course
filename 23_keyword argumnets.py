# keyword argumnets = argumnets precedad by an identifier when we pass them to a funtion
#                     The order of the argumnets doesn't matter, unlike positional argumnets
#                     Python knos the names of the argumnets that our function receives

def hello(first,middle,last):
    print('Hello '+first+' '+middle+' '+last)

hello(last='Poveda',first='Angel',middle='Moises')