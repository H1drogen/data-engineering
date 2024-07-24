import json
import logging
import random
import boto3
import datetime
import requests

s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')
logger = logging.getLogger()

# event = {
#     "monster": 'giant-badger'
# }

def lambda_handler(event, context):
    url = f"https://www.dnd5eapi.co/api/monsters/{event['monster']}"
    payload = {}
    headers = {
        'Accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        payload = {
            "dice_type": "d20",
            "dice_count": 2
        }
        lambda_client.invoke(
            FunctionName='roll_dice',
            InvocationType='Event',
            Payload=json.dumps(payload)
        )
        s3.put_object(
            Bucket='mybucket20240718102437846400000001',
            Key=event['monster'],
            Body=response.text
        )
        logger.info('monster saved')

    else:
        logger.error('monster does not exist')
        print('monster does not exist')

    return {
        'statusCode': response.status_code,
    }
