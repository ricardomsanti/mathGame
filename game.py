from datetime import datetime
import random as rd



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
    now = datetime.now().strftime("%H:%M:%S:%SS")
    return now



#sum
def sum_generate(min, max, now):
    op_log = {}
    answer = ""
    min = int(min)
    max = int(max)
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 + n2
    question = input("{} + {} =  ".format(n1, n2))
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({"sum" + now : {
                    "op" : "sum" ,
                    "time" : now ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))


#subtraction

def subtraction_generate(min, max, now):
    op_log = {}
    answer = ""
    min = int(min)
    max = int(max)
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 - n2
    question = input("{} - {} =  ".format(n1, n2))
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({"sub" + now : {
                    "op" : "sum" ,
                    "time" : now ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))


def times_generate(now):
    op_log = {}
    answer = ""
    min = 1
    max = 10
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 * n2
    question = input("{} * {} =  ".format(n1, n2))
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({"times" + now : {
                    "op" : "sum" ,
                    "time" : now ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))


def division_generate(max, now):
    op_log = {}
    answer = ""
    
    max = int(max)
    
    zero_div = [ x for x  in range(max) if x % max == 0]
    
    
    #division by zero error---fix it
    min = rd.choice(zero_div)
    n1 = rd.randint(min, max)
    n2 = rd.randint(min, max)
    result = n1 * n2
    question = input("{} * {} =  ".format(n1, n2))
    if int(question) == result:
        answer = "right"
    else:
        answer = "wrong"
        
    op_log.update({"division" + now : {
                    "div" : "sum" ,
                    "time" : now ,
                    "answer" : answer
                        }
                    })
    return op_log
        
    
    print("{} + {} = {} ".format(n1, n2, result))



#---------------------------------------------------------------
rounds = int(set_rounds())

min = set_min()
max = set_max()
main_log = {}

for x in range(rounds):
    main_log[x] = times_generate(op_time())
for x, y in main_log.items():
    print(x, y)
#subtraction

#times

#division

