import boto3

# Connect to local Floci
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

# Create bucket
s3.create_bucket(Bucket="resume-storage")
print('Created S3 bucket')

# # List buckets
response = s3.list_buckets()

# print("Buckets:")
for bucket in response["Buckets"]:
    print(bucket["Name"])

