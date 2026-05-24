import boto3
import json

lambda_client = boto3.client(
    "lambda",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

payload = {
    "name": "Nagendra"
}

response = lambda_client.invoke(
    FunctionName="Hello-Lambda",

    Payload=json.dumps(payload)
)

result = json.loads(
    response["Payload"].read()
)

print(result)
