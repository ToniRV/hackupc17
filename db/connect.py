#!/bin/python3
from urllib.parse import quote_plus
import pymongo

with open('key.txt') as f:
    passcode = f.read()

uri = 'mongodb://%s:%s>@cluster0-shard-00-00-yhrrp.mongodb.net:27017,cluster0-shard-00-01-yhrrp.mongodb.net:27017,cluster0-shard-00-02-yhrrp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin' % ('upc', passcode)
client = pymongo.MongoClient(uri)
db = client.accounts
