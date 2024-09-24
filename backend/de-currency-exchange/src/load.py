import json
import datetime

import boto3


def lambda_handler(event, context):
    """Writes the data to a date-encoded S3 folder.

    The folder structure should make it easy to locate rates from a given date and time.

    Args:
        event: dictionary in the same format as the output from the transform function
        context: supplied by AWS

    Returns:
        dictionary, either {'result': 'Success'} if successful or {'result': 'Failure'} otherwise
    """
    # replace this code
    client = boto3.client('s3', region_name='eu-west-2')

    client.put_object(Bucket='nc-de-currency-data-20240805125909831800000003',
                      Key=f"/{datetime.date.today().strftime('%Y-%m-%d')}/eur", Body=bytes(json.dumps(event), 'utf-8'))

    return {"result": "Success"}



