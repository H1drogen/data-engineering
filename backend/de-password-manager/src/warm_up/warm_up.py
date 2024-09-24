import boto3
import os
from dotenv import load_dotenv

load_dotenv()
s3_client = boto3.client('s3')

bucket = os.getenv('BUCKET_NAME')


def initiate_bucket():
    s3_client.create_bucket(bucket, CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'})
    s3_client.put_object(Body='./text1.txt', Bucket=bucket, Key='text1')
    s3_client.put_object(Body='./text2.txt', Bucket=bucket, Key='text2')


def show_files():
    s3_client.list_objects_v2(bucket)

def delete_resources():
    pass