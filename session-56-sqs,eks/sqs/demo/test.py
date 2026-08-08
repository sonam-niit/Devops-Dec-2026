import boto3

REGION = "us-east-1"
QUEUE_NAME = "order-queue"

sqs = boto3.client(
    "sqs",
    region_name=REGION
)

queue_url = sqs.get_queue_url(
    QueueName=QUEUE_NAME
)["QueueUrl"]

print("Using queue:", queue_url)

messages = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=5
)

print(messages)