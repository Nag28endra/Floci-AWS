import os 
import boto3 
from botocore.exceptions import ClientError

BUCKET_NAME = 'resume-storage'
DATA_FOLDER = 'data'

# connect to flcoi
s3 = boto3.client( 
    "s3", 
    endpoint_url="http://localhost:4566", 
    aws_access_key_id="test", 
    aws_secret_access_key="test", 
    region_name="us-east-1" 
    )

# Check and create Bucket if not created.
try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print(f'Bucket {BUCKET_NAME} already exists!')
except ClientError:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f'Bucket {BUCKET_NAME} is created!')

# Upload files
for filename in os.listdir(DATA_FOLDER):
    file_path = os.path.join(DATA_FOLDER,filename)

    # skip directories
    if os.path.isdir(file_path):
        continue

    print(f'Uploading file: {filename}')

    s3.upload_file(
        file_path,
        BUCKET_NAME,
        filename
    )

print('All files are uploaded')

# List down the files that are uploaded to the bucket
response = s3.list_objects_v2(Bucket=BUCKET_NAME)
print('Files inside the Bucket')

if "Contents" in response:
    for obj in response['Contents']:
        print('-',obj['Key'])
else:
    print('Bucket is empty')

