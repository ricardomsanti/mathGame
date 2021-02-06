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
op_reps = gc.op_selector(round_num=round_num)
random_mode = gc.set_random()

#RUN CHALLENGE
##################################################################################
gc.run_store(op_reps=op_reps, random_mode=random_mode, round_num=round_num,min=min, max=max, dict_time=gc.set_time,id=gc.set_id) 

