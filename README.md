# mongodb-examples

MongoDB Python script examples


# Links

* https://www.mongodb.com/docs/manual/reference/
* https://www.mongodb.com/docs/v4.4/tutorial/write-scripts-for-the-mongo-shell/
* https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
* https://www.mongodb.com/docs/manual/reference/method/db.getCollection/


# Starting

 mkdir /u/data/mongo
 /opt/homebrew/bin/mongod --dbpath /u/data/mongo

# Create a new DB

 use github
 show dbs

## Add data

 db.user.insertOne({name: "Ada Lovelace", age: 205})

```
github> db.user.insert({name: "Ada Lovelace", age: 205})
DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('656a849cfb7e29f5b58a8860') }
}
github> show collections
user
```









# Useful Commands


| Shell Helpers            | JavaScript Equivalents               |
|:------------------------:|:-------------------------------------------:|
| show dbs, show databases | db.adminCommand('listDatabases')            |
| use <db>                 | db = db.getSiblingDB('<db>')                |
| show collections         | db.getCollectionNames()                     |
| show users               | db.getUsers()                               |
| show roles               | db.getRoles({showBuiltinRoles: true})       |
| show log <logname>       | db.adminCommand({ 'getLog' : '<logname>' }) |
| show logs                | db.adminCommand({ 'getLog' : '*' })         |
| it                       | cursor = db.collection.find()
                             if ( cursor.hasNext() ){
                                 cursor.next();
                              }                                          |


# Notes




# Markdown Notes
  
* https://markdown.land/markdown-table

## Command


# Misc Notes

* db.version()
* db.stats()
* db.watch()




