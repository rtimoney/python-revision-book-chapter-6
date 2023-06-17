# RETURNING RESULTS - PAGE 78

num = input('Enter an integer :')

def square(num) :
    if not num.isdigit() :
        return 'Invalid entry'
    
    # cast input (read initially as a string) as an integer
    num = int(num)
    return num * num

print(num , 'Squared Is :' , square(num))



