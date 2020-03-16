# Тестовое задание
Использовано:
* Django
* Celery + Redis (для асинхронных задач)
* Nginx
## Usage:
    $ docker-compose up
---
#### admin-panel  
  login: admin  
  password: 123456
## API
### POST /api/add 
json request:
```json
{
  "status": "",
  "result": "",
  "addition": {
    "uuid": "<uuid>",
    "value": "<value>"
  },
  "description": {}
}
```
json response:
```json
{
  "status": "<http_status>",
  "result": "<bool:operation_status>",
  "addition": {
    "uuid": "<uuid>",
    "balance": "<balance>"
  },
  "description": {}
}
```
### POST /api/substract
json request:
```json
{
  "status": "",
  "result": "",
  "addition": {
    "uuid": "<uuid>",
    "value": "<value>"
  },
  "description": {}
}
```
json response:
```json
{
  "status": "<http_status>",
  "result": "<bool:operation_status>",
  "addition": {
    "uuid": "<uuid>",
    "balance": "<balance>",
    "hold": "<hold>"
  },
  "description": {}
}
```
### POST /api/status
json request:
```json
{
  "status": "",
  "result": "",
  "addition": {
    "uuid": "<uuid>"
  },
  "description": {}
}
```
json response:
```json
{
  "status": "<http_status>",
  "result": "<bool:operation_status>",
  "addition": {
    "uuid": "<uuid>",
    "balance": "<balance>",
    "hold": "<hold>",
    "status": "<status>"
  },
  "description": {}
}
```
### GET /api/ping
json response:
```json
{
  "status": "<http_status>",
  "result": "<bool:operation_status>",
  "addition": {},
  "description": {}
}
```
## Errors
json format in case of an error:
```json
{
  "status": "<http_status>",
  "result": "False",
  "addition": {},
  "description": {
    "error": "<message>"
  }
}
```
