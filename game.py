from datetime import datetime as dt
import random as rd
import game_ops as go
from pymongo import MongoClient
from account_services import Account 
#---------------------------------------------------------------


ac = Account(client=MongoClient("localhost", 27017))
db_math = ac.db_math
col_math = ac.col_math(db_math)





"""
Challenge
    Rounds?
        How many?
        Proportion?




round_num = int(go.set_rounds())

min = go.set_min()
max = go.set_max()
dic_time = go.op_time()
main_log = {}

for x in range(rounds):
    main_log[x] = sum_generate(min, max, op_time(), set_id())
for x, y in main_log.items():
    print(x, y)
"""#subtraction
op_dict = go.op_selector(round_num=round_num)
for x, y in op_dict.items():
    print(x, y)


