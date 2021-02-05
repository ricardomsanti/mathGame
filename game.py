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
    rounds = input("Please set the number of rounds \n")
    return rounds
    
def op_time():
    dict_time = { "year" : dt.now().year,
                "day" : dt.now().day,
                "month" : dt.now().month ,
                "hour" : dt.now().hour,
                "minute" : dt.now().minute,
                "second" : dt.now().second}
    return dict_time
        
    



#sum
#---------------------------------------------------------------------------------------
def sum_generate(min, max, dict_time, id):
    op_log = {}
    answer = ""
    min = int(min)
    max = int(max)
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 + n2
    t1 = dt.now().second
    
    question = input("{} + {} =  ".format(n1, n2))
    t2 = dt.now().second
    delta_time = t2 - t1
    
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
    
    op_log.update({id : {
                    "op" : "sum" ,
                    "time" : dict_time ,
                    "answer" : answer,
                    "delta_time" : delta_time 
                                    }
                                })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))


#subtraction

def subtraction_generate(min, max,dict_time, id):
    op_log = {}
    answer = ""
    min = int(min)
    max = int(max)
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 - n2
    t1 = dt.now().second
    question = input("{} - {} =  ".format(n1, n2))
    t2 = dt.now().second
    delta_time = t2 - t1
    
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({id : {
                    "op" : "sum" ,
                    "time" : dict_time ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))


def times_generate(now, dict_time, id):
    op_log = {}
    answer = ""
    min = 1
    max = 10
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 * n2
    t1 = dt.now().second
    question = input("{} * {} =  ".format(n1, n2))
    t2 = dt.now().second
    delta_time = t2 - t1
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({id: {
                    "op" : "sum" ,
                    "time" : dict_time ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))


def division_generate(max, now, dict_time, id):
    op_log = {}
    answer = ""
    
    max = int(max)
    
    zero_div = [ x for x  in range(max) if x % max == 0]
    
    
    #division by zero error---fix it
    min = rd.choice(zero_div)
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 * n2
    t1 = dt.now().second
    question = input("{} * {} =  ".format(n1, n2))
    t2 = dt.now().second
    delta_time = t2 - t1
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({id : {
                    "div" : "sum" ,
                    "time" : dict_time ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))



#---------------------------------------------------------------
rounds = int(set_rounds())

min = set_min()
max = set_max()
dic_time = op_time()
main_log = {}

for x in range(rounds):
    main_log[x] = sum_generate(min, max, op_time(), set_id())
for x, y in main_log.items():
    print(x, y)
#subtraction

#times

#division

