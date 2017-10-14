#!/bin/python3
from pprint import pprint
import pymongo

with open('key.txt') as f:
#with open('key.txt') as f:
    passcode = f.read()

uri = 'mongodb://%s:%s@cluster0-shard-00-00-yhrrp.mongodb.net:27017,cluster0-shard-00-01-yhrrp.mongodb.net:27017,cluster0-shard-00-02-yhrrp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin' % ('upc', 'hackupc')
client = pymongo.MongoClient(uri)
demoset = client.accounts.demo

def get_balance():
    return demoset.find().sort([('$natural', -1)])[0]

def get_subscriptions():
    return demoset.find({
        'subCat': {
            '$ne': 'noSubCat'
        }
    })

def get_subscription_spending():
    pipe = [{'$match': {'subCat': {'$ne': 'noSubCat'}}},
            {'$group': {'_id': None,
                        'sum': {'$sum': "$amount"}}}]
    return demoset.aggregate(pipeline=pipe)

if __name__=="__main__":
    for res in get_subscription_spending():
        pprint(res)
