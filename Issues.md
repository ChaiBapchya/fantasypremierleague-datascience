# 1. Inspect element issue

While checking the source of any webpage - Directly Inspect element of Value visible on Webpage isnt always helpful

Thanks to http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/

- Realization 
.
1. User(Client) Requests using Browser
2. Reaches the Server
3. Data can be fetched and injected into the Template and send as a Response back to the Client
	i.e. Server side Page creation
	OR
	Client side Web App - 
4. Server sends the Static content HTML page
but Data -  Javascript in the server response fetches the data from an API and uses it to create the page client-side

To get such data - Developer tools - Network - XHR (instead of normal HTML )
```
#html_doc = urllib2.urlopen("https://fantasy.premierleague.com/drf/bootstrap-static").read()
#print(html_doc[1])
```

When u make a HTTP Request, if we read it using urllib
It treats the response as a String
Hence despite the format was in JSON, Errors like 
1. TypeError: string indices must be integers, not str
2. AttributeError str-object-has-no-attribute

Hence use other library that treats Request - Response as Json 

# 2. Attribute error
```
names.append(full_name.str())
AttributeError: 'unicode' object has no attribute 'str'
```
Solution - 
```
str(full_name)
```

# 3. Unicode Encode Error
```
names.append(str(full_name))
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 1: ordinal not in range(128)
```
Solution
```
s = full_name.encode('ascii', 'ignore').decode('ascii')
```
Disadv - removes all other internationalizations


# 4. Unicode - String
```
', u'ElliotEmbleton', u'DeclanRice']
```
To get rid of u'
Convert Unicode string to normal ascii string
```
str(variable)
```

# 5. Type error
```
response = requests.get("https://fantasy.premierleague.com/drf/entry/"+main_user_id+"/event/"+gameweek+"/picks")
TypeError: cannot concatenate 'str' and 'int' objects
```
Solution
```
str(main_user_id)
```

# 6. Name error
```
if player["is_captain"]==true:
NameError: name 'true' is not defined
  if player["is_captain"]===true:                             ^
SyntaxError: invalid syntax
```

Solution
```
if player["is_captain"]:
```

# 7. Type Error - NoneType
```
TypeError: 'NoneType' object has no attribute '__getitem__'
```
At times some data depends on User Login - Such data is not returned in JSON response as visible in Postman or HTTP request's corr. response

However visible in Browser->Network->XHR->response part
To know what data was sent while making such a request - rightclick - Get cURL -
for e.g.
For - https://fantasy.premierleague.com/a/team/3146257/event/19

Actual URL was
```
curl 'https://fantasy.premierleague.com/drf/bootstrap-dynamic' -H 'Host: fantasy.premierleague.com' -H 'User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: https://fantasy.premierleague.com/a/team/3146257/event/19' -H 'Cookie: _ga=GA1.2.309538033.1473872047; __gads=ID=1e26f8a1f937797f:T=1476526048:S=ALNI_MYwwjDM8utxJfBY-D7A1smdFhSnIA; csrftoken=GcIusuHLJOCxMHiZ1wbI8IsqkcybWq2t; _ga=GA1.3.309538033.1473872047; pl_profile="eyJzIjogIld6SXNNemc1TkRjME5GMDoxY05MRlY6TFE0aE0yWTI4WFhOaTdqeW04c1lqdXU2Nk4wIiwgInUiOiB7ImxuIjogIkJhcGF0IiwgImZjIjogOCwgImlkIjogMzg5NDc0NCwgImZuIjogIkNoYWl0YW55YSJ9fQ=="; sessionid=".eJyrVkpPzE2NT85PSVWyUirISSvIUdJRik8sLcmILy1OLYpPSkzOTs1LAUsmVqYW6UEFivUCwHwnqDyKpkyg-mhDHWMLSxNzE5PYWgBVoiN7:1cNcq5:gyTfZ4HaGrHPDIPnYJh0O6NGLKs"; _gat=1; _dc_gtm_UA-33785302-1=1' -H 'Connection: keep-alive'
```
Here actual Sessions, parameters, tokens were passed




# 8. Value Error
```
Traceback (most recent call last):
  File "user.py", line 23, in <module>
    json_data = json.loads(response.text)
  File "/usr/lib64/python2.7/json/__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/usr/lib64/python2.7/json/decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib64/python2.7/json/decoder.py", line 382, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
```

 - Solution - 
 Handle the exception (basically bad request)


# 9. URL issue
```
File "user.py", line 36, in <module>
    response = requests.get("https://fantasy.premierleague.com/drf/entry/"+str(counter))
  File "/usr/lib/python2.7/site-packages/requests/api.py", line 71, in get
    return request('get', url, params=params, **kwargs)
  File "/usr/lib/python2.7/site-packages/requests/api.py", line 57, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python2.7/site-packages/requests/sessions.py", line 475, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python2.7/site-packages/requests/sessions.py", line 585, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python2.7/site-packages/requests/adapters.py", line 403, in send
    timeout=timeout
  File "/usr/lib/python2.7/site-packages/requests/packages/urllib3/connectionpool.py", line 578, in urlopen
    chunked=chunked)
  File "/usr/lib/python2.7/site-packages/requests/packages/urllib3/connectionpool.py", line 385, in _make_request
    httplib_response = conn.getresponse(buffering=True)
  File "/usr/lib64/python2.7/httplib.py", line 1136, in getresponse
    response.begin()
  File "/usr/lib64/python2.7/httplib.py", line 453, in begin
    version, status, reason = self._read_status()
  File "/usr/lib64/python2.7/httplib.py", line 409, in _read_status
    line = self.fp.readline(_MAXLINE + 1)
  File "/usr/lib64/python2.7/socket.py", line 480, in readline
    data = self._sock.recv(self._rbufsize)
  File "/usr/lib64/python2.7/ssl.py", line 756, in recv
    return self.read(buflen)
  File "/usr/lib64/python2.7/ssl.py", line 643, in read
    v = self._sslobj.read(len)
    `` 
```

# 10. Connection Error
```
Traceback (most recent call last):
File "gw_player_python.py", line 20, in <module>
response = requests.get("https://fantasy.premierleague.com/drf/entry/"+str(main_user_id)+"/event/"+str(gameweek)+"/picks")
File "/usr/lib/python2.7/dist-packages/requests/api.py", line 55, in get
return request('get', url, kwargs)
File "/usr/lib/python2.7/dist-packages/requests/api.py", line 44, in request
return session.request(method=method, url=url, kwargs)
File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 335, in request
resp = self.send(prep, send_kwargs)
File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 438, in send
r = adapter.send(request, kwargs)
File "/usr/lib/python2.7/dist-packages/requests/adapters.py", line 327, in send
raise ConnectionError(e)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='fantasy.premierleague.com', port=443): Max retries exceeded with url: /drf/entry/197156/event/1/picks (Caused by <class 'socket.error'>: [Errno 104] Connection reset by peer)
```
Solution:
Check for the response and if it returns in any error - query after 5 sec sleep
```
response=''
        while response == '':
                try:
                        #url="10.0.0.0"
                        url="https://fantasy.premierleague.com/drf/entry/"+str(main_user_id)+"/event/"+str(gameweek)+"/picks"
                        response = requests.get(url)
                except:
                        print "Connection refused"
                        time.sleep(5)
                        continue
        player_data_per_gw.append(main_user_id)
        if(response.status_code!=200):
                print "na"
                player_data_per_gw.append("empty")
        else:
                print "200"
                json_data = json.loads(response.text)

```

# 11. Package error
```
mongoimport -d fpl_users -c fpl_user_data --type csv --file data.csv --headerline
bash: mongoimport: command not found...
Packages providing this file are:
'mongodb-org-tools'
'mongo-tools'
```

```
dnf install mongodb-org-tools
Failed to synchronize cache for repo 'dockerrepo', disabling.
Last metadata expiration check: 0:27:04 ago on Thu Jan  5 11:01:05 2017.
Error: package mongodb-org-tools-3.2.0-1.el7.x86_64 conflicts with mongodb-server provided by mongodb-server-3.2.8-2.fc25.x86_64
(try to add '--allowerasing' to command line to replace conflicting packages)
```

- Solution
```
dnf install mongo-tools
```

# 12. Operation failed

- Problem - 
 ```
 db.fpl_user_data.find().sort({KEY:1})
Error: error: {
	"waitedMS" : NumberLong(0),
	"ok" : 0,
	"errmsg" : "Executor error during find command: OperationFailed: Sort operation used more than the maximum 33554432 bytes of RAM. Add an index, or specify a smaller limit.",
	"code" : 96
}
```

- Solution    
http://pe-kay.blogspot.in/2016/05/how-to-change-mongodbs-sort-buffer-size.html

```
db.adminCommand({"setParameter":1,"internalQueryExecMaxBlockingSortBytes":134217728})
{ "was" : 33554432, "ok" : 1 }
> db.fpl_user_data.find().sort({KEY:1})
```

# 13. Unsorted output
```
db.fpl_user_data.find().sort({KEY:"main_user_id"})
Error: error: {
	"waitedMS" : NumberLong(0),
	"ok" : 0,
	"errmsg" : "bad sort specification",
	"code" : 2
}
```

- Issue - Output was not coming in sorted fashion

- Solution
```
db.collection_name.find().sort({key:1}).pretty()

db.fpl_user_data.find().sort( { main_user_id: 1 } ).pretty()
```

# 14. Access Mongo using Python

- Problem - Accesing MongoDB using Python

https://docs.mongodb.com/getting-started/python/client/
https://docs.mongodb.com/getting-started/python/query/

# 15. Aggregation

https://docs.mongodb.com/getting-started/python/aggregation/

# 16. Data inconsistency

1. Incomplete

- count - 193212
- last elemet id 198181

2. empty data fields (ASCII Unicode)

- first name last name
- main user team name

3. duplicate data

- Solution
```
>db.collection-name.remove({'key':'value'})
```

- key = attribute name / field / column name
- value = corresponding value

# 17. Performance Increase

- Trying to Improve the Speed / Rate of Requests from 1 request per second to 10 or more
- Tried Python libraries
1. Twisted
2. Grequests 

- Grequest is better but gave following errors
1. 
```
('Connection aborted.', error(22, 'Invalid argument'))
```
2. 
```
HTTPSConnectionPool(host='fantasy.premierleague.com', port=443): Max retries exceeded with url: /drf/entry/2365060 (Caused by NewConnectionError('<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7f9b6dcf1e50>: Failed to establish a new connection: [Errno 110] Connection timed out',))
```
3. 
```
No JSON object could be decoded
```
