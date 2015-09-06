KyivTalks
========

Project for sharing thoughts about Kyiv's places


How to install
========


```
$ cd <name_of_the_project>
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python db_create.py   
(venv) $ python db_migrate.py
```


Example
========

```
$ curl -i -X POST -H "Content-Type: application/json" -d '{ "email" : "saniasutula3@gmail.com", "password" : "demodemo1234" }' http://127.0.0.1:5000/api/new_user

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 27
Location: http://127.0.0.1:5000/api/users/1

{ "email": "saniasutula3@gmail.com", "id": 1 }

```


```
$ curl -u saniasutula3@gmail.com:demodemo1234 -i -X GET http://127.0.0.1:5000/api/token
HTTP/1.0 200 OK
Content-Type: application/json

{
  "duration": 600,
  "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc"
}
```

```
$ curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc:x -i -X GET http://127.0.0.1:5000/api/resource
HTTP/1.0 200 OK
Content-Type: application/json

{
  "data": "Hello, <user.login>!"
}
```