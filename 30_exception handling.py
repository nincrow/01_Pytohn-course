# exception =   events detected during execution that interrupt the flow of a program

from typing import final


try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!! moron!!")
except ValueError as e:
    print(e)
    print("Enter only number plz")
except Exception as e:
    print(e)
    print("something went wrong  :(")
else:
    print(result)
finally:
    print('This will always execute')