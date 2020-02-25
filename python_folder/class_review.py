'''
review nov 8
'''
import random


class WackyNum:

    eating_incident = {6, 7, 8, 9}

    @staticmethod
    def eating_check(a ,b):
        if a in WackyNum.eating_incident and b in WackyNum.eating_incident:
            print('awkward because of the eating incident')

    def __init__(self, num=0):
        self.num = num

    def __repr__(self):
        return f"I am approx {self.num + random.randint(-2, 2)}"

    def __add__(self, in_num):
        print('nums getting big, eh?')
        WackyNum.eating_check(self.num, in_num)
        if type(self.num) is int:
            return WackyNum(self.num + in_num)
        raise MemoryError(f'I don\'t remeber asking for a {type(in_num)}')

if __name__ == '__main__':
    my_num = WackyNum(8)
    WackyNum.eating_check(6,7)
    print(my_num)
    my_num = my_num+100
    print(my_num)
    #my_num = my_num + 'a'
    print(my_num)

