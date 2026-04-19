# REST API Tetsing using Postman

- Download Postman tool
- for basic API test no need to cretae any account
- you can directly Test

- use any Fake api for Test

## Get Request

- URL: https://jsonplaceholder.typicode.com/todos
- Get Method
- click on send (you can see all 200 todos)
- also check status code which 200 OK

## Get By ID

- URL: https://jsonplaceholder.typicode.com/todos/1
- Get Method change url with ID number
- click on send (you can see all perticular ID todo)
- also check status code which 200 OK

## POST Method

- URL: https://jsonplaceholder.typicode.com/todos
- Post Method
- body, raw (choose JSON)
- type below JSON Data

```json
{
    "userId": 1,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
}
```
- click on send (you can see all 200 todos)
- also check status code which 201 OK
- check response with new id (201)

## PUT Method

- URL: https://jsonplaceholder.typicode.com/todos/2
- /2 means 2nd POSt data I want to update
- PUT Method
- body, raw (choose JSON)
- type below JSON Data

```json
{
    "userId": 1,
    "id": 2,
    "title": "this is my updated title",
    "completed": true
}
```
- click on send see data updated
- also check status code which 200 OK
- check response with updated data

## Delete By ID

- URL: https://jsonplaceholder.typicode.com/todos/1
- Delete Method (change url with ID number) like which data you want to delete
- click on send
- you can see data deleted with empty response
- also check status code which 200 OK