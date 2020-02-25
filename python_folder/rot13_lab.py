'''
ROT 13 lab
written by Rhornberger
last updated oct 28 2019
'''
# create a function to Rotate a word 13 spots 
import string
def rot(a):
    a = user_input # reassign the passed in string for ease of use later in the function
    letter = string.ascii_lowercase
    output = ''
    b = input('would you like to pick the number of rotation?: ').lower() # this gives the user the option to pick a custom rotation or not
    if b == 'yes': # this will use the custom rotation if chosen
        c = int(input('What rotation would you like to use?: '))
        for char in a:
            output += letter[(a.find(char)+c)%26]
        return output
    else: # otherwise this will run using the sandard 13 for rotation
        for char in a:
            output += letter[(a.find(char)+13)%26]
        return output
# take user input and return the answers
user_input = input('What word would you like to obscure?: ').lower()
print(rot(user_input))
