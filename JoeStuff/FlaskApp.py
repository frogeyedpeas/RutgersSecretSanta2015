from pymongo import MongoClient
from flask import Flask

from datetime import datetime

@app.root("/")
def showForm():
    

def putData():
    client = MongoClient("localhost:27017") # creates a client
    db = client.primer                      # assigning primer database to db
    db = client['primer']                   # or use this! MAGIC!
    
    db.dataset                              # access the dataset collection
    db['dataset']                           # or like this! MAGIC!
    
    coll = db.dataset                       # assign the dataset collection to coll
    coll = db['dataset']                    # or type this! MAGIC!

    result = db.santa.insert_one(
        {
            "interests": ["interest":""],
            "coal":["don't_get":""]
            "name":""
            "phone_number":"000-000-0000"
        }
    )

if __name__ == "__main__":
    app.run()
