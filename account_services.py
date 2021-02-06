from pymongo import MongoClient
  

class Account:
    
    dash = "==================================================================================================="
    client = MongoClient("localhost", 27017)
    db = client["MATH"]
    
    #Checks if the collection's name provided by the user already exists. If not, it creates one.
                    
    def col_math(self):
        print()
        print("MATH GAME STARTED")
        print(self.dash)
        register = input("Do you already have an account?[y/n]\n")
        if register !="y":
            account = input("Please, type your account username.\n")
            account_col = self.client.get_collection(account)
        else:
            account = input("Please, type a username for your account.\n")
            account_col = self.client[account]
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