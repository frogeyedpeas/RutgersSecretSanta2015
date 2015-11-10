from pymongo import MongoClient
from datetime import datetime

def MongoTest():
    client = MongoClient("localhost:27017") # creates a client
    db = client.primer                      # assigning primer database to db
    db = client['primer']                   # or use this! MAGIC!
    
    db.dataset                              # access the dataset collection
    db['dataset']                           # or like this! MAGIC!
    
    coll = db.dataset                       # assign the dataset collection to coll
    coll = db['dataset']                    # or type this! MAGIC!

    result = db.restaurants.insert_one(
        {
            "address": {
                "street":"Broadway Street",
                "zipcode":"10027",
                "city":"New York",
                "state":"NY",
                "building":"3153",
                "coord":"40.8145922, -73.9594182",
            },
            "borough":"manhattan",
            "cuisine":"indian",
            "grades": [
                {
                    "date": datetime.strptime("2014-6-05","%Y-%m-%d"),
                    "grade":"A",
                    "score":15
                },
                {
                    "date": datetime.strptime("2014-12-06","%Y-%m-%d"),
                    "grade": "C",
                    "score": 12
                }
            ],
            "name": "Chapati House",
            "restaurant_id":"0021413"
        }
    )

    print("ID Used: "+"00221413")
    print("Interted ID: "+str(result.inserted_id))

if __name__ == "__main__":
    MongoTest()
