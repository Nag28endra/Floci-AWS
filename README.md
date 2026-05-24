# Floci AWS S3 Examples

This repository contains simple Python examples for working with **Floci** using **boto3**.

## What is boto3?

**boto3** is the official AWS SDK for Python. It lets you write Python code to interact with AWS services such as S3, EC2, Lambda, and more.

In this project, boto3 is used to connect to a **local Floci endpoint** and perform S3 operations like:
- creating buckets
- uploading files
- listing objects
- deleting objects
- deleting buckets

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd floci-aws
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Floci using Docker

Use Docker to start the Floci service on port `4566`:

```bash
docker run --rm -d --name floci -p 4566:4566 floci
```

If your Floci image requires extra environment variables, you can start it like this:

```bash
docker run --rm -d --name floci -p 4566:4566 -e SERVICES=s3 -e AWS_DEFAULT_REGION=us-east-1 floci
```

After the container starts, confirm it is running:

```bash
docker ps
```

## Using Floci with boto3

The scripts in this repository connect to Floci using a local endpoint URL:

```python
import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)
```

### Why these credentials?

Floci does not need real AWS credentials. The example uses placeholder values:
- `aws_access_key_id = "test"`
- `aws_secret_access_key = "test"`

## Examples available

### 1. Create bucket

File: `create_bucket_s3.py`

This script:
- connects to Floci
- creates the bucket `resume-storage`
- lists all buckets

Run it:

```bash
python create_bucket_s3.py
```

### 2. Upload files

File: `upload_files_s3.py`

This script:
- connects to Floci
- checks whether the bucket exists
- uploads all files from the `data/` folder to `resume-storage`
- lists the uploaded objects

Run it:

```bash
python upload_files_s3.py
```

### 3. Delete files and bucket

File: `delete_files_s3.py`

This script:
- connects to Floci
- deletes all objects in `resume-storage`
- deletes the bucket

Run it:

```bash
python delete_files_s3.py
```

### 4. Lambda examples

Folder: `lambda-function/`

These scripts show how to create, invoke, and delete a Lambda function in Floci.

#### Deploy Lambda

File: `deploy_lambda.py`

This script:
- connects to the Lambda endpoint in Floci
- reads `lambda.zip`
- creates a Lambda function named `Hello-Lambda`

Run it:

```bash
cd lambda-function
python deploy_lambda.py
```

#### Invoke Lambda

File: `invoke_lambda.py`

This script:
- connects to Floci
- invokes the `Hello-Lambda` function
- sends a JSON payload

Run it:

```bash
cd lambda-function
python invoke_lambda.py
```

Example output:

```json
{"message": "Hello Nagendra"}
```

#### Delete Lambda

File: `delete_lambda.py`

This script:
- connects to Floci
- deletes the `Hello-Lambda` function

Run it:

```bash
cd lambda-function
python delete_lambda.py
```

### 5. Logging system example

Folder: `projects/logging-system/`

This project contains a logging example that:
- creates a local log directory
- writes a log file
- uploads it to S3 in Floci

Install its dependencies:

```bash
cd projects/logging-system
pip install -r requirements.txt
```

Run the example:

```bash
python logger_system.py
```

## Example workflow

A typical workflow for this repository is:

1. Start Floci with Docker
2. Create the bucket
3. Upload files
4. Verify the objects
5. Delete files and bucket when finished

Example sequence:

```bash
python create_bucket_s3.py
python upload_files_s3.py
python delete_files_s3.py
```

### Lambda workflow

A typical Lambda workflow in this repository is:

1. Start Floci with Docker
2. Deploy the Lambda function
3. Invoke the Lambda function
4. Delete the Lambda function when finished

Example sequence:

```bash
cd lambda-function
python deploy_lambda.py
python invoke_lambda.py
python delete_lambda.py
```

## Notes

- The current S3 examples assume the bucket name is `resume-storage`.
- Files in the `data/` folder are used by the upload example.
- The Lambda examples use the function name `Hello-Lambda`.
- The project uses `boto3` and `botocore` from `requirements.txt`.
