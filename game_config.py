from datetime import datetime as dt
import random as rd
import game_ops as go
from pymongo import MongoClient

#########################################################################################################
#CONFIGURATIONS
#########################################################################################################

dash = "======================================================================"

def set_start():
    print()
    print("MATH CHALLENGE STARTED")
    print(dash)
    print() 
    print("Let's start round configuration")
 
        
    
        
    
        



def set_id():
    alpha1 = [x for x in "aeiou"]
    symbol = [y for y in "!@#$%&_+="]
    num = rd.randint(1,100.000)
    id = rd.choice(alpha1) + rd.choice(symbol) + str(num)
    return id


def set_min():
    min = input("Please set operations minumum value \n\n")
    return min

def set_max():
    max = input("Please set operations maximum value \n\n")
    return max

def set_rounds():
    round_num = input("Please set the number of rounds \n\n")
    return round_num
    
def set_time():
    dict_time = { "year" : dt.now().year,
                "day" : dt.now().day,
                "month" : dt.now().month ,
                "hour" : dt.now().hour,
                "minute" : dt.now().minute,
                "second" : dt.now().second}
    return dict_time
        
def op_selector():    
    
    
    op_list = [ "sum", "sub", "times", "div"] 
    op_reps = ""
    num_assigned = 0
    total = 0
    for x in op_list:
        num = input("Please define how many {} operations rounds there will be in this game \n\n".format(x))
        num = int(num)
        total += num
        op_reps += str(num) + ","
        
    print("Round total = {}".format(total))
    return op_reps



def set_random():
    random = input("Set shuffle mode on? \n\n")
    return random
    
def run_store(op_reps, random_mode, min, max, dict_time, id):
      
    
    sum_count, sub_count, times_count, div_count = op_reps.split(',')[:-1]
    sum_count= int(sum_count)
    sub_count = int(sub_count)
    times_count = int(times_count)
    div_count = int(div_count)
    
    
    ops = [1,2,3,4]
    main_log = {}
    end_ops = 0
    
      
    #generating randomness-----------------------------------
    
    if random_mode == "y":
    
        while end_ops < 4:

            running_op = rd.choice(ops)
            
            if running_op == 1:
                sum_count -= 1            
                if sum_count >= 0:                
                    main_log.update(go.sum_generate(min=min, max=max, dict_time=set_time(), id=set_id()))
                
                else:
                    if sum_count == -1:
                        end_ops += 1
                    else:
                        continue
                
            elif running_op == 2:
                sub_count -= 1
                if sub_count >= 0:                
                    main_log.update(go.subtraction_generate(min=min, max=max, dict_time=set_time(), id=set_id()))
                else:
                    if sub_count == -1:
                        end_ops += 1
                    else:
                        continue
            
            elif running_op == 3:    
                times_count -=1
                if times_count >= 0:                
                    main_log.update(go.times_generate(dict_time=set_time(),id=set_id()))
                else: 
                    if times_count == -1:
                        end_ops += 1
                    else:
                        continue

            elif running_op == 4:
                div_count -= 1
                if div_count >= 0:                
                    main_log.update(go.division_generate(max=max, dict_time=set_time(), id=set_id()))
                else: 
                    if div_count == -1:
                        end_ops += 1
                    else:
                        continue

    return main_log                
    
        
        
    
    