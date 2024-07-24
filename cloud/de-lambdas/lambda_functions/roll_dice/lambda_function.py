import json
import logging
import random
import boto3
import datetime

s3 = boto3.client('s3')
logger = logging.getLogger()

# event = {
#   "dice_type": "d20",
#   "dice_count": 2
# }

def lambda_handler(event, context):
    dice = event['dice_type']

    def dice_roll():
        return random.randint(1, int(dice[1:]))

    results = []
    for i in range(event['dice_count']):
        results.append(dice_roll())

    logger.info(f'Rolled: {results}')
    print(f'Rolled: {results}')
    with open('/tmp/history.txt', 'a') as file:
        file.write(f'\nRolled: {results} at {datetime.datetime.now()}')

    response = s3.list_buckets()
    s3.upload_file('/tmp/history.txt', 'mybucket20240718102437846400000001', 'history.txt')
    print(response)

    return {
        'statusCode': 200,
        'body': f'Rolled: {results}'
    }