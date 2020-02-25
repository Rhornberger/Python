'''
Number to Roman Nmeral lab 
numbers 1-100
written by Rhornberger
last updated oct 28 2019
'''
#build the dictionaries
ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
ten = {10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX'}
tenths = {0: '', 1: '', 2: 'XX', 3: 'XXX', 4: 'XIL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}

#build the function
def roman(a):
    if a[0] == '0':
        return 'The number zero is not accounted for in Roman numerals.'
    elif len(a) == 1:
        a1 = int(a)
        return ones[a1]
    elif len(a) == 2 and a[0] == '1':
        a1 = int(a)
        return ten[a1]
    elif len(a) == 2:
        a1 = int(a)// 10
        b1 = int(a) % 10
        res = tenths[a1] + ones[b1]
        return res
    elif a == '100':
        return 'C'
    return 'The number you have input is outside of my code parameters. Please try again with a different number'

user_input = input('Please enter the number you would like translated into roman numerals: ')

print(roman(user_input))