# Storing Functions

# allows us to call funtions from the cat module
import cat

#allow the user to set a name for pet which will override the pet default when we call the functions from cat.py

pet = input('Enter a pet name :')
cat.lick(pet)
cat.nap(pet)
cat.purr(pet)

# we can also use an alias for the module as shown below 
import cat as anothername

petagain = 'Garfield'

anothername.lick(petagain)
anothername.nap(petagain)
anothername.purr(petagain)

