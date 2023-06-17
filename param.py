# Adding Parameters

# define a function with three params which simply returns thise params 
def echo(user , lang , sys) :
    print('User :' , user , 'Language :', lang , 'Platform :' , sys)

# pass string argumengts to the function params in the order in which they appear
echo('Mike' , 'Python' , 'Windows')

# pass string arguments by specififying the corresponding params
echo( lang='Python' , sys='Mac OS' , user='Anne')

# as echo includes no default for its params, we will

# define another function with default values
def mirror(user = 'Carole' , lang = 'Python') :
    print('\nUser :' , user , '\t\tLanguage :' , lang)

# will return the default values
mirror()

# default user , override the language
mirror(lang='Java')

# override user (which is the first param) and return default language
mirror('Tony')

# override both params 
mirror('Susan' , 'C++')