'''
Practice strings
written by Rhornberger
last updated oct 26 2019
'''
# baseline string problem 0
'''
def add(a, b):
    return a + b
print(add(8, 8))
print(add(7, 7))
'''
# double letters problem 1
'''
def double_letter(x):
    return ''.join([i * 2 for i in x])
#print(double_letter('hello'))
print(double_letter('fuck off!'))
'''
# misssing character problem 2
#def missing_char(a):

# return th eletter that appears latest in the alphabet problem 3
'''
def latest_letter(a):
    letter = a.lower()
    letter1 = sorted(letter)
    letter2 = letter1.pop()
    return letter2
#print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis'))
#print(latest_letter('udfhybiysdbguyhPNIERUIHBTGUYGUHBIUVFYR'))
'''
# count the number of time hi is in the listproblem 4
'''
def count_hi(a):
    a = a.lower()
    count = a.count('h')
    return count
#print(count_hi('hihihihihihi'))
print(count_hi('hihi'))
'''

# count the number of occurances of a word in a list (was for problem 4 but not what they are asking)
'''
def word_count(a):
    counts = dict()
    words = a.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count('hi hi'))
'''
# return tru if the number of 'cat' and the number of 'dog' is =
#def cat_dog(a):


# count the letters in a word problem 6
'''
def count_letter(letter, word):
    return word.count(letter)
#print(count_letter('i', 'antidisestablishmentterianism'))
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))
'''
# convert a string to lowercase and with no white space problem 7
'''
def convert(a):
    convert1 = a.lower()
    con2 = convert1.strip()
    return con2
print(convert('    HELLO WORLD   '))
'''


