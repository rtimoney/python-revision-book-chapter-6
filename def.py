# Defining Blocks

# custom functions in Python are defined using the def keyword as follows :

#def functionname() :
#    print('Line 1')
#    print('Line 2')
#    print('Final Line')

#functionname()

global_var = 1

def my_vars() : 
    print('Global variable :' , global_var)

    local_var = 2 
    print('Local variable :' , local_var)

    global inner_var
    inner_var = 3


my_vars()

print('Second Global variable :' , inner_var)
