from pymongo import MongoClient

client = MongoClient("localhost:27019") # creates a client
db = client.primer                      # assigning primer database to db
db = client['primer']                   # or use this! MAGIC!

db.dataset                              # access the dataset collection
db['dataset']                           # or like this! MAGIC!

coll = db.dataset                       # assign the dataset collection to coll
coll = db.['dataset']                   # or type this! MAGIC!
