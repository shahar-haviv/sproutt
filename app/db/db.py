import pymongo

conn_str = "mongodb://localhost:27017"

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.list_database_names())
except Exception:
    print("Unable to connect to the server.")

db = client.xternity
