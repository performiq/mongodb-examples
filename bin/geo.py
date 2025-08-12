#!/usr/bin/env python

import sys
import pymongo

HOST=  "127.0.0.1"

client = pymongo.MongoClient(HOST, 27017)

db = client.geo

journeys = db.journeys.find()

print(journeys)


for tuple in journeys:
    print(tuple[key1])
    print(tuple[key2])



