import boto3
import json
import time

REGION = "us-east-1"
QUEUE_NAME = "order-queue"

sqs = boto3.client(
    "sqs",
    region_name=REGION
)

queue_url = sqs.get_queue_url(
    QueueName=QUEUE_NAME
)["QueueUrl"]

while True:
    messages = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10
    )
    if "Messages" in messages:
        for msg in messages["Messages"]:
            order = json.loads(msg["Body"])
            print("Processing order: ",order)
            
            print(f"Email send for order {order['orderId']}")
            
            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg["ReceiptHandle"]
            )
    else:
        print("No messages.....")
        time.sleep(5)