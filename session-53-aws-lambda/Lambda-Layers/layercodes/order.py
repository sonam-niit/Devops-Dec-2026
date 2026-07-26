import json
from logger import get_logger
logger = get_logger("Order Event")
def lambda_handler(event, context):
    logger.info("Processing Order Event");
    logger.debug(f"Event Details: {json.dumps(event)}")
    return {
        'statusCode': 200,
        'body': json.dumps('Order Processed Successfully!')
    }