from pymongo import MongoClient
  

class Account:
    
    dash = "==================================================================================================="
    def __init__(self, client):
        self.client = client

    #Checks if the collection's name provided by the user already exists. If not, it creates one.
    
        
    def db_math (self, client):
        math_database = client["MATH"]
        return math_database
        
        
    def col_math(self, db):
        print()
        print("MATH GAME STARTED")
        print(dash)
        register = input("Do you already have an account?[y/n]\n")
        if register !="y":
            account = input("Please, type your's account username.\n")
            account_col = db.get_collection(account)
        else:
            account = input("Please, type a username for your account.\n")
            account_col = db.account
        return account_col
            
            
        
        
"""        

        
            
client = MongoClient("localhost", 27017)
db_names = client.database_names()
db = client.get_database("db_name")
col_names = db.list_collection_names
col = db.get_collection("col_name")
col.find()
col.count()
col.insert()
col.update()
col.remove()

"""