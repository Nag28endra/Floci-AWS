import boto3
from pathlib import Path
lambda_client = boto3.client(  
    "lambda",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

zipped_lambda_path = Path("lambda.zip")
with open(zipped_lambda_path, 'rb') as f:
    zipped_code = f.read()

response = lambda_client.create_function(
    FunctionName='Hello-Lambda',
    Runtime='python3.9',
    Role='arn:aws:iam::000000000000:role/lambda-role',
    Handler='lambda_function.handler',
    Code={'ZipFile': zipped_code},
    Description='A simple Lambda function',
    Publish=True
)

print(response)