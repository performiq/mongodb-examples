#!/usr/bin/env python

import sys
import pymongo

print(f"VERSION |{sys.version}|")

HOST=  "203.3.69.35"

client = pymongo.Mongoclient(HOST, 27017)

#parameter can be the database URL

db = client.dataBase

dbOutput = db.collection.find()

for tuple in dbOutput:
    print tuple[key1]
    print tuple[key2]



