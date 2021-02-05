from datetime import datetime as dt
import random as rd



def set_id():
    alpha1 = [x for x in "aeiou"]
    symbol = [y for y in "!@#$%&_+="]
    num = rd.randint(1,100.000)
    id = rd.choice(alpha1) + rd.choice(symbol) + str(num)
    return id


def set_min():
    min = input("Please set operations minumum value \n")
    return min

def set_max():
    max = input("Please set operations maximum value \n")
    return max





def set_rounds():
    round_num = input("Please set the number of rounds \n")
    return round_num
    
def set_time():
    dict_time = { "year" : dt.now().year,
                "day" : dt.now().day,
                "month" : dt.now().month ,
                "hour" : dt.now().hour,
                "minute" : dt.now().minute,
                "second" : dt.now().second}
    return dict_time
        
def op_selector(round_num):    
    
    print("Total round number = {} \n".format(round_num))
    op_list = [ "sum", "subtraction", "times", "division"] 
    op_dict = {}
    total = round_num
    num_assigned = 0
    for x in op_list:
        num = input("Please define how many {} operations rounds there will be in this game \n".format(x))
        num = (int(num))
        num_assigned += num
        rest = total - num_assigned
        op_dict[x] = num
        print("{} rounds left".format(rest))
    return op_dict
