from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.get_database("MATH")

db2 =client.get_database("main_logs")


   
client = MongoClient("localhost",27017)
db = client.get_database("MATH")
col = db.get_collection("user")

"""

#lacking some fixes in order the provide multiple users
def user_log():
    
    user = input("Please insert a username \n")
    user_list = db.collection_names()
    user_coll = db.get_collection("user")
    check = user in user_list
    
    if check:
        print("Welcome player {}".format(user))
    else:
        print("Welcome player {}".format(user))
        user_coll.insert_one({"user":user})
        
    return user
        
"""        


def save_logs(main_log):
    
    for x, y in main_log.items():
        print(x,y)
    

    log_col = db2.get_collection("main_logs")
    log_col.insert_one(main_log)
    print("Results saved successfuly. \n"
        "See you next time!")
        
        
