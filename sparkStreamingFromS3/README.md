# Spark Streaming from S3 Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![Apache Spark](https://img.shields.io/badge/Apache-Spark-orange.svg)](https://spark.apache.org/)
[![S3](https://img.shields.io/badge/AWS-S3-blue.svg)](https://aws.amazon.com/s3/)
[![Scala](https://img.shields.io/badge/Scala-Programming-red.svg)](https://www.scala-lang.org/)

> **Note: This repository is archived and no longer actively maintained.**

Apache Spark streaming examples demonstrating real-time data processing from Amazon S3, including file monitoring, data ingestion, and stream processing for large-scale data analytics.

## 📁 Project Structure

- **[lambda.py](lambda.py)** - Lambda function for S3 event processing
- **[stream.scala](stream.scala)** - Spark streaming application
- **[autoscaling_rule.json](autoscaling_rule.json)** - EMR autoscaling configuration
- **[lifecycle_rule.json](lifecycle_rule.json)** - S3 lifecycle management

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **EMR Cluster**: Amazon EMR cluster with Spark
3. **S3 Bucket**: S3 bucket for data storage and processing
4. **Lambda Function**: For S3 event processing

### Setup

1. **Create S3 bucket:**
   ```bash
   aws s3 mb s3://your-spark-streaming-bucket
   ```

2. **Create EMR cluster:**
   ```bash
   aws emr create-cluster \
       --name "SparkStreaming" \
       --release-label emr-6.x.0 \
       --applications Name=Spark \
       --ec2-attributes KeyName=your-key-pair \
       --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge \
       --instance-groups InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge
   ```

3. **Deploy Lambda function:**
   ```bash
   # Package and deploy Lambda
   zip -r lambda.zip lambda.py
   aws lambda create-function \
       --function-name s3-spark-trigger \
       --runtime python3.8 \
       --handler lambda.handler \
       --zip-file fileb://lambda.zip
   ```

## 🔧 Examples Covered

### Spark Streaming
- **Real-time processing**: Processing data streams in real-time
- **S3 integration**: Reading data from S3 buckets
- **Stream processing**: Continuous data processing
- **Window operations**: Time-based window aggregations

### S3 Event Processing
- **File monitoring**: Monitoring S3 for new files
- **Event triggers**: Lambda functions for S3 events
- **Data ingestion**: Automatic data ingestion pipeline
- **File processing**: Processing new files as they arrive

### EMR Integration
- **Cluster management**: EMR cluster configuration
- **Autoscaling**: Automatic cluster scaling
- **Resource optimization**: Optimizing cluster resources
- **Monitoring**: Cluster and job monitoring

## 📚 Examples Overview

### Spark Application
- **stream.scala**: Main Spark streaming application
- **S3 file processing**: Reading and processing S3 files
- **Stream operations**: Real-time data transformations

### Lambda Function
- **lambda.py**: S3 event processing Lambda function
- **Event handling**: Processing S3 object creation events
- **Trigger management**: Managing Spark job triggers

### Configuration Files
- **autoscaling_rule.json**: EMR autoscaling configuration
- **lifecycle_rule.json**: S3 lifecycle management rules

## 🛠️ Running Examples

### Deploy Spark Application
```bash
# Submit Spark streaming job
spark-submit \
    --class SparkStreamingApp \
    --master yarn \
    --deploy-mode cluster \
    stream.scala
```

### Test S3 Integration
```bash
# Upload test file to S3
aws s3 cp test-data.csv s3://your-spark-streaming-bucket/input/

# Monitor Lambda execution
aws logs tail /aws/lambda/s3-spark-trigger --follow
```

### Monitor EMR Cluster
```bash
# Check cluster status
aws emr describe-cluster --cluster-id your-cluster-id

# Monitor applications
aws emr list-instances --cluster-id your-cluster-id
```

## 🔌 Spark Streaming Examples

### Basic S3 Streaming
```scala
// Spark streaming from S3
val spark = SparkSession.builder()
    .appName("S3Streaming")
    .getOrCreate()

val stream = spark.readStream
    .format("csv")
    .option("header", "true")
    .load("s3://your-bucket/input/*")

val query = stream.writeStream
    .outputMode("append")
    .format("console")
    .start()
```

### Window Operations
```scala
// Time-based window aggregations
val windowedStream = stream
    .groupBy(
        window($"timestamp", "5 minutes"),
        $"category"
    )
    .agg(count("*").as("count"))
```

### Lambda Integration
```python
# Lambda function for S3 events
import boto3
import json

def handler(event, context):
    s3 = boto3.client('s3')
    emr = boto3.client('emr')
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Trigger Spark job
        response = emr.add_job_flow_steps(
            JobFlowId='your-cluster-id',
            Steps=[
                {
                    'Name': 'Spark Streaming Job',
                    'ActionOnFailure': 'CONTINUE',
                    'HadoopJarStep': {
                        'Jar': 'command-runner.jar',
                        'Args': [
                            'spark-submit',
                            '--class', 'SparkStreamingApp',
                            's3://your-bucket/jars/stream.jar'
                        ]
                    }
                }
            ]
        )
    
    return {'statusCode': 200}
```

## ⚠️ Important Notes

- **Cluster Costs**: EMR clusters incur costs while running
- **Data Latency**: S3 streaming has inherent latency
- **Resource Management**: Monitor cluster resources and costs
- **Error Handling**: Implement robust error handling
- **Monitoring**: Set up comprehensive monitoring and alerting

## 🔗 Related Examples

- **[bigdatabattle/](../bigdatabattle/)** - Big data processing examples
- **[serverlessPipeline/](../serverlessPipeline/)** - Serverless data processing
- **[athena/](../athena/)** - Alternative data querying

## 📖 Documentation

- [Apache Spark Streaming Documentation](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
- [EMR Spark Documentation](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html)
- [S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html)
- [Lambda S3 Integration](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)

## 🎯 Use Cases

### Real-time Analytics
- **Log processing**: Real-time log analysis
- **Clickstream analysis**: User behavior tracking
- **IoT data processing**: Sensor data streaming
- **Financial data**: Real-time financial analytics

### Data Processing
- **ETL pipelines**: Real-time data transformation
- **Data validation**: Continuous data quality checks
- **Aggregation**: Real-time data aggregation
- **Enrichment**: Data enrichment and joining

### Monitoring and Alerting
- **Anomaly detection**: Real-time anomaly detection
- **Performance monitoring**: System performance tracking
- **Business metrics**: Real-time business intelligence
- **Operational dashboards**: Live operational metrics

## 💡 Best Practices

### Performance Optimization
- **Partitioning**: Use appropriate S3 partitioning
- **Compression**: Compress data for faster processing
- **Caching**: Cache frequently accessed data
- **Resource allocation**: Optimize cluster resources

### Reliability
- **Checkpointing**: Use Spark checkpointing for fault tolerance
- **Error handling**: Implement comprehensive error handling
- **Monitoring**: Monitor job progress and performance
- **Backup**: Backup configurations and data

### Cost Optimization
- **Spot instances**: Use spot instances for cost savings
- **Autoscaling**: Implement intelligent autoscaling
- **Resource monitoring**: Monitor and optimize resource usage
- **Lifecycle management**: Implement S3 lifecycle policies

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 