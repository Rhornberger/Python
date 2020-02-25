'''
practice fundemantals
written by Rhornberger
last updated oct 25 2019
'''
# addition function
'''
practice making functions
def add(a,b):
    return a + b
print(add(6,6))
print(add(7,3))
'''

# even or not function with /
'''
def is_even(a):
    res = a / 2
    if res % 2  == 0:
        return 'True'
    else:
        return 'False'
    
print(is_even(9))
'''

# even or not function with //
'''
def is_even(a):
    res = a // 2
    if res % 2 == 0:
        return 'True'
    else:
        return 'False'
print(is_even(9))
#this will not work to find even because the // (floor division) will not print the
    decimal places and will only ever return a whole number and because we are dividing
    by 2 to find even will only ever return a whole number giving us truly inconsistent 
    results.
'''
# even or not function with %
'''
def is_even(a):
    res = a % 2
    if res == 0:
        return 'True'
    return 'False'
print(is_even(9))
this is the most concise option to find an even number out of the presented options for
    this part of the lab. I skips the extra step of the modulus = 0 on the if statement 
    line
'''
# opposites lab if either number is negative retun true problem two
'''
def opposite(a, b):
    if (a < 0) and (b < 0):
        return 'false'
    elif (a < 0) or (b < 0):
        return 'true'
    else:
        return 'false'
print(opposite(-1, 6))
print(opposite(2, 7))
print(opposite(-2, -3))
'''

# within 10 of 100
'''
def near_100(num):
    if num in range(90, 111):
        return 'True'
    return 'False'
print(near_100(97))
'''
# max of 3 parameters
'''
def max_of_three(a, b, c):
    num = (a, b, c)
    return max(num)
print(max_of_three(6, 8, 9))
'''

# powers of 2
''''

def powers_0f_2(num):
    if num in range(2, 21):
        res = 2 ** num
        return res
    return 'Number not in range.'
print(powers_0f_2(2))
'''
# practice for pulling a specific number
'''
def div(x):
    res = x[1] 

    return res
print(div(367))
'''