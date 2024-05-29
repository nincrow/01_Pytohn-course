# scope = The region tht a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped version of a variable can be created

name = 'Angel'      # global scope (available inside & outside functions)

def display_name():
    name = 'Poveda'     # local scope (available only inside this function)
    print(name)

print(name)
display_name()

# PRIORIDAD EN VARIABLES
# L = LOCAL,  E = ENCLOSING,   G = GLOBAL,  B = BUILT-IN