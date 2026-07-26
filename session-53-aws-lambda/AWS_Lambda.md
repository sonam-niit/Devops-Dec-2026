## AWS Lambda Service
### Create Function
- Select Author from scratch
- give function name: myfirstfunction
- select Python
- create
- check the code (keep the default code)
- click on Deploy
- After that go to function Test tab
- try to test the function check the result details
- you can see you are able to execute function
- click on logs -> which redirects you to cloudwatch where you can see LogManagement -> LogGroup(named with your function name) - check Logs

## Trigger Function From an API

- Go to Lambda Function
- select your Lambda 
- click on add Trigger Button
- select API Gateway
- create new API
- Select Rest API -> Security (Open)
- you can see endpoint
- trigger that endpoint and check results