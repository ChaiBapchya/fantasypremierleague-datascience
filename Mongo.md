# Steps for Mongo Installation, Setup, Start, Use
1. 
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
2.
```
systemctl start mongod
```
3.
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
