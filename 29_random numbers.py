# pseudo - random
import random

x = random.randint(1,6)
y = random.random() #random number between 0 ~ 1

myList =['rock','paper','scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J",'Q','K','A']

random.shuffle(cards)

print(cards)