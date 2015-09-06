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

How to install front-end
========
```
cd frontend
npm run build
```

API Documentation
========

- POST **/api/new_user**
Register new user. The body must contain a JSON object that defines `login`, `email` and `password`.

- GET **/api/users/&lt;int:id&gt;**
Return a user by `id`.

- GET **/api/token**
Return a token for user.

- GET **/api/places**
Return a list of all places.

- GET **/api/places/&lt;int:id&gt;**
Return a place by `id`.

- POST **/api/places/new_place**
Create a new place. The body must contain a JSON object that defines `name`,`address` and `description`.

- POST **/api/images/new_image**
Upload a new image. The body must contain a JSON object that defines `url` and `place_id`.

- POST **/api/ratings/new_rating**
Give some place a score. The body must contain a JSON object that defines `user_id`,`place_id` and `score`.

- POST **/api/comments/new_comment**
Create a new comment. The body must contain a JSON object that defines `place_id`,`text`,`user_id` and `anonimity`.

- GET **/api/search_place/<string>**
Search places by `string`.

Example
========

Create new user:
```
$ curl -i -X POST -H "Content-Type: application/json" -d '{ "email" : "saniasutula3@gmail.com", "password" : "demodemo1234" }' http://127.0.0.1:5000/api/new_user

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 27
Location: http://127.0.0.1:5000/api/users/1

{ "email": "saniasutula3@gmail.com", "id": 1 }

```

Get token:
```
$ curl -u saniasutula3@gmail.com:demodemo1234 -i -X GET http://127.0.0.1:5000/api/token
HTTP/1.0 200 OK
Content-Type: application/json

{
  "duration": 600,
  "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc"
}
```

Test route
```
$ curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc:x -i -X GET http://127.0.0.1:5000/api/resource
HTTP/1.0 200 OK
Content-Type: application/json

{
  "data": "Hello, <user.login>!"
}
```
