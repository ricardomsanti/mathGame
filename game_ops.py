from datetime import datetime as dt
import random as rd


#########################################################################################################
#OPERATIONS
#########################################################################################################


# sum
#---------------------------------------------------------------------------------------
def sum_generate(min, max, dict_time, id, reps):
    
    for x in range(reps -1):
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


# subtraction
#---------------------------------------------------------------------------------------


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

# times
#---------------------------------------------------------------------------------------

def times_generate(dict_time, id):
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

# division
#---------------------------------------------------------------------------------------

def division_generate(max, dict_time, id):
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
