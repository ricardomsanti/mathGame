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


min = gc.set_min()
max = gc.set_max()
op_reps = gc.op_selector()
random_mode = "y"   #gc.set_random() temporarily disabled until coding new steps

#RUN CHALLENGE
##################################################################################
main_log = gc.run_store(op_reps=op_reps, random_mode=random_mode, min=min, max=max, dict_time=gc.set_time(),id=gc.set_id()) 

for x, y in main_log.items():
    print(x,y)
