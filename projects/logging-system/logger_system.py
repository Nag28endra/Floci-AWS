import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

BUCKET_NAME = "loci-logs-dev"  # bucket name
LOCAL_LOG_FOLDER = "./logs"

# create local log folder
os.makedirs(LOCAL_LOG_FOLDER, exist_ok=True)
s3 = boto3.client( "s3", 
    endpoint_url="http://localhost:4566", 
    aws_access_key_id="test", 
    aws_secret_access_key="test", 
    region_name="us-east-1"
)

# create the bucket
try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' already exists.")
except ClientError as e:
    s3.create_bucket(Bucket=BUCKET_NAME) 
    print(f"Bucket '{BUCKET_NAME}' created")

# Generate log content
now = datetime.now() 
date_folder = now.strftime("%Y-%m-%d") 
time_file = now.strftime("log_%H-%M-%S.log") 
log_content = f""" 
==================================== 
APPLICATION LOG 
==================================== 
Timestamp : {now} 
Status : SUCCESS 
Message : Logging system working successfully 
==================================== 
"""

# Save log to local file
local_log_path = os.path.join(LOCAL_LOG_FOLDER, date_folder)

with open(local_log_path, "w") as log_file:
    log_file.write(log_content)
print(f"Log saved locally at: {local_log_path}")

# s3 object path
s3_key = f"{date_folder}/{time_file}"

# upload file to s3
s3.upload_file(
    local_log_path,
    BUCKET_NAME,
    s3_key 
)

print(f"Log uploaded to S3 at: s3://{BUCKET_NAME}/{s3_key}")

# list log files
print('Stored Logs:')
response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=date_folder)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"- {obj['Key']}")    
else:
    print("No logs found in S3.")
