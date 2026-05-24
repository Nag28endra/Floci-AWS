import boto3

lambda_client = boto3.client(
    "lambda",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

response = lambda_client.delete_function(
    FunctionName="Hello-Lambda"
)

print("Lambda function deleted successfully!")
