#  IMPORTING FUNCTIONS - (Chapter 6 - Creating Functions) page 82  

# dog will be a module which stores functions to be made available to other files in the program

def bark(pet = 'A Dog') :
    print( pet , 'Says WOOF !')

def lick(pet = 'A Dog') :
    print( pet , 'Drinks water')

def nap(pet = 'A Dog') :
    print( pet , 'Sleeps in the sun')

# for larger programs we can import modules into other modules in order to create a module hierarchy

