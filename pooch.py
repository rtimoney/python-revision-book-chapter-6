#  IMPORTING FUNCTIONS - (Chapter 6 - Creating Functions) page 82  

from dog import bark , lick , nap

# when we import individual function names the module name does not get imported so it cannot be used as a prefix
# eg we can't use : dog.bark()


bark()
lick()
nap()

bark('Pooch')
lick('Pooch')
nap('Pooch')
