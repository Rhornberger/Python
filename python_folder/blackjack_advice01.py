'''
advanced blackjack advice
written by Rhornberger
last update oct 28 2019
'''
# build the dictionary 
b_dict = {'ace': [1, 11], 'a': [1, 11], 'two': 2, '2': 2, 'three': 3, '3': 3, 'four': 4, '4': 4, 'five': 5, '5': 5, 'six': 6, '6': 6, 'seven': 7, '7': 7, 'eight': 8, '8': 8, 'nine': 9, '9': 9,  'ten': 10, '10': 10, 'jack': 10, 'j': 10, 'queen': 10, 'q': 10, 'king': 10, 'k': 10}
# build a function
def blackjack(a, b, c):
    num = b_dict[a] + b_dict[b] + b_dict[c]
    num1 = b_dict[a] + b_dict[b]
    #num2 = b_dict[a] + b_dict[c]
    #num3 = b_dict[b] + b_dict[c]
    if a or b or c != 'ace' or 'a':
        if num < 17:
            print(f'{num} Not high enough you should hit')
        elif num in range(17,21):
            print(f'{num} You should stay')
        elif num == 21:
            print(f'{num} Winner, Winner chicken dinner! You hit Blackjack')
        elif num > 21:
            print(f'{num} You busted')
    elif a or b or c == 'ace' or 'a':
        if c == 'ace' or 'a':
            if num1 >= 10:
                res = num1 + (b_dict[c][1::])
                return res



#take the user input
d = input('What is your first card?: ').lower()
e = input('What is you second card?: ').lower()
f = input('What is your third card?: ').lower()
#return the result
print(blackjack(d, e, f))

