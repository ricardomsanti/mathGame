from datetime import datetime as dt
import random as rd
import game_ops as go
from pymongo import MongoClient
import game_config as gc
import game_ops as go
#---------------------------------------------------------------

#PROGRAM STARTED
##################################################################################

gc.set_start()

#CHALLENGE CONFIGURATION
##################################################################################

round_num = gc.set_rounds()
min = gc.set_min()
max = gc.set_max()
op_selection = gc.op_selector(round_num=round_num)
random = gc.set_random()

#RUN CHALLENGE
##################################################################################


sum_count = int(op_selection["sum"])
sub_count = int(op_selection["sub"])
times_count = int(op_selection["times"])
div_count = int(op_selection["div"])

#---------------------------------------------------some proble here

result_dict = {}
if random != "y":
    for round in round_num:
        result_dict.update(go.sum_generate(min=min, max=max, dict_time=gc.set_time(),id=gc.set_id(),reps=sum_count))
        