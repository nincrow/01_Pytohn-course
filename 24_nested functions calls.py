# nested functions calls = functions calls inside other function calls innermost function calls are resolved first returned value is used as argumnet for the outer funciton

#num = input('Enter a whole positive number: ')
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input('Enter a whole positive number: ')))))