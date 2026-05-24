import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = 'resume-storage'

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1" 
)

try:
    # List down all the files of the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    # Delete files of the bucket
    if "Contents" in response:
        for obj in response['Contents']:
            filename = obj['Key']
            print(f'Deleting File: {filename}')
            s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
    else:
        print('Bucket is empty')
    
    # Delete Bucket
    print(f'Deleting Bucket: {BUCKET_NAME}')
    s3.delete_bucket(Bucket=BUCKET_NAME)

except ClientError as e:
    print('Error:', e)

