#!/usr/bin/env python

import sys
import pymongo

print(f"VERSION |{sys.version}|")

HOST=  "203.3.69.35"
HOST=  "127.0.0.1"

client = pymongo.MongoClient(HOST, 27017)

db = client.geo

data = db.journey.find()

for tuple in data:
    print(tuple)

