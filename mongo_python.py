from pymongo import MongoClient
client = MongoClient()
db = client.fpl_users
coll = db.fpl_user_data
#cursor = db.fpl_user_data.find()
#for document in cursor:
#    print(document)

cursor = db.fpl_user_data.aggregate(
    [
        {"$group": {"_id": "$main_user_region", "count": {"$sum": 1}}}
    ]
)

for document in cursor:
	if document['_id'].upper()=='ENGLAND':
 		print document
