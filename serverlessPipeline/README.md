# Serverless Data Pipeline Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/lambda/)
[![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue.svg)](https://aws.amazon.com/dynamodb/)
[![Kinesis](https://img.shields.io/badge/AWS-Kinesis-green.svg)](https://aws.amazon.com/kinesis/)
[![Firehose](https://img.shields.io/badge/AWS-Firehose-purple.svg)](https://aws.amazon.com/kinesis/data-firehose/)

> **Note: This repository is archived and no longer actively maintained.**

Serverless data pipeline examples demonstrating real-time data processing using AWS Lambda, DynamoDB, Kinesis, and Kinesis Firehose for scalable data ingestion and processing.

## 📁 Project Structure

- **[DynamoDBToFirehose.py](DynamoDBToFirehose.py)** - DynamoDB to Firehose data streaming
- **[writeToDynamoDB.py](writeToDynamoDB.py)** - Writing data to DynamoDB
- **[writeToKinesis.py](writeToKinesis.py)** - Writing data to Kinesis streams
- **[web.py](web.py)** - Web interface for data pipeline
- **[test.py](test.py)** - Pipeline testing utilities
- **Policy files**: IAM policies for various services

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Python**: Python 3.7 or higher
4. **IAM Permissions**: Proper permissions for all services

### Setup

1. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

2. **Install Python dependencies:**
   ```bash
   pip install boto3 flask requests
   ```

3. **Create required AWS resources:**
   ```bash
   # Create DynamoDB table
   aws dynamodb create-table \
       --table-name data-pipeline \
       --attribute-definitions AttributeName=id,AttributeType=S \
       --key-schema AttributeName=id,KeyType=HASH \
       --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
   ```

## 🔧 Pipeline Architecture

### Data Flow
```
Web Interface → Lambda → DynamoDB → Firehose → S3
                ↓
              Kinesis Stream
```

### Components
- **Web Interface**: Data input and monitoring
- **Lambda Functions**: Data processing and transformation
- **DynamoDB**: Real-time data storage
- **Kinesis**: Stream processing
- **Firehose**: Data delivery to S3
- **S3**: Data lake storage

## 📚 Examples Overview

### Data Ingestion
- **writeToDynamoDB.py**: Direct DynamoDB writes
- **writeToKinesis.py**: Kinesis stream ingestion
- **web.py**: Web-based data input

### Data Processing
- **DynamoDBToFirehose.py**: Stream processing pipeline
- **Lambda functions**: Real-time data transformation

### Testing and Monitoring
- **test.py**: Pipeline testing utilities
- **Policy files**: IAM permissions for services

## 🛠️ Running Examples

### Start Web Interface
```bash
cd serverlessPipeline/
python web.py
```

### Test Data Ingestion
```bash
python test.py
```

### Deploy Lambda Functions
```bash
# Package and deploy Lambda functions
aws lambda create-function \
    --function-name dynamodb-to-firehose \
    --runtime python3.8 \
    --handler DynamoDBToFirehose.lambda_handler \
    --zip-file fileb://function.zip
```

## 🔌 Pipeline Components

### DynamoDB Integration
```python
# Writing to DynamoDB
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('data-pipeline')

table.put_item(
    Item={
        'id': 'unique-id',
        'data': 'sample-data',
        'timestamp': '2024-01-01T00:00:00Z'
    }
)
```

### Kinesis Integration
```python
# Writing to Kinesis
import boto3
kinesis = boto3.client('kinesis')

kinesis.put_record(
    StreamName='data-stream',
    Data='sample-data',
    PartitionKey='partition-key'
)
```

### Firehose Integration
```python
# Firehose delivery
import boto3
firehose = boto3.client('firehose')

firehose.put_record(
    DeliveryStreamName='data-delivery-stream',
    Record={'Data': 'sample-data'}
)
```

## ⚠️ Important Notes

- **Costs**: Monitor usage of all services to control costs
- **Permissions**: Ensure proper IAM roles and policies
- **Scaling**: Be aware of service limits and quotas
- **Data Retention**: Configure appropriate data retention policies
- **Monitoring**: Set up CloudWatch alarms for pipeline health

## 🔗 Related Examples

- **[lambda_frameworks/](../lambda_frameworks/)** - Lambda function examples
- **[athena/](../athena/)** - Data querying and analysis
- **[bigdatabattle/](../bigdatabattle/)** - Big data processing

## 📖 Documentation

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [Kinesis Documentation](https://docs.aws.amazon.com/kinesis/)
- [Firehose Documentation](https://docs.aws.amazon.com/firehose/)

## 🎯 Use Cases

### Real-time Analytics
- **User behavior tracking**: Real-time user interaction data
- **IoT data processing**: Sensor data streaming
- **Log analysis**: Application log processing

### Data Warehousing
- **ETL pipelines**: Extract, transform, load processes
- **Data lake ingestion**: S3 data lake population
- **Real-time dashboards**: Live data visualization

### Event Processing
- **Clickstream analysis**: Web traffic analysis
- **Fraud detection**: Real-time fraud monitoring
- **Recommendation engines**: Real-time recommendations

## 💡 Best Practices

- **Error Handling**: Implement robust error handling
- **Monitoring**: Set up comprehensive monitoring
- **Cost Optimization**: Monitor and optimize costs
- **Security**: Implement proper security measures
- **Testing**: Test pipeline components thoroughly

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 