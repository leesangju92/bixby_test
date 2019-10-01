import pymongo
uri = "mongodb://3.230.56.3"
username = "developer"
password = "dev123"
authSource = 'winery_bixby'
authMechanism = 'SCRAM-SHA-1'
client = pymongo.MongoClient(uri, username=username, password=password, authSource=authSource, authMechanism=authMechanism)
database = client['winery_bixby']
collection = database['wine_collection']

def find_query(query={}):
    find = list(collection.find(query))
    # 각 wine의 id가 Object 형식이라 문자열로 변환
    for wine in find:
        wine["_id"] = str(wine["_id"])
    return find
