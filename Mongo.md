# Steps for Mongo Installation, Setup, Start, Use
1. Installation
```
dnf install mongodb mongodb-server
```

- Installed:
```
  boost-program-options.x86_64 1.60.0-10.fc25                                   
  boost-regex.x86_64 1.60.0-10.fc25                                             
  mongodb.x86_64 3.2.8-2.fc25                                                   
  mongodb-server.x86_64 3.2.8-2.fc25                                            
  mozjs38.x86_64 38.8.0-2.fc25                                                  
  yaml-cpp.x86_64 0.5.1-13.fc24     
```
In order to use, `mongo-import`, install following - 
```
dnf install mongo-tools
```

2. Start
```
systemctl start mongod
```
3. Use
```
[root@chai chai]# mongo
MongoDB shell version: 3.2.8
connecting to: test
  
use fpl_users;
switched to db fpl_users
> db
fpl_users
> db.createCollection("fpl_user_data");
{ "ok" : 1 }

show collections
fpl_user_data
```
4. Mongo-import

Absolute path - data.csv
```
mongoimport -d fpl_users -c fpl_user_data --type csv --file data.csv --headerline
2017-01-05T11:54:03.753+0530	connected to: localhost
2017-01-05T11:54:04.338+0530	imported 19214 documents
```
All CSV files imported similarly

```
db.fpl_user_data.find().pretty()
```
