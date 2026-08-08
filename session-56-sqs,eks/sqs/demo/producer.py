import boto3
import json
import uuid 

REGION = "us-east-1"
QUEUE_NAME = "order-queue"

sqs = boto3.client(
    "sqs",
    region_name=REGION
)

queue_url = sqs.get_queue_url(
    QueueName=QUEUE_NAME
)["QueueUrl"]

order = {
    "orderId":str(uuid.uuid4()),
    "user":"Bob",
    "amount":3500,
    "status":"CREATED"
}
# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(order)
)

print("Order sent to queue",response['MessageId'])