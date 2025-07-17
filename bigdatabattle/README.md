# Big Data Battle Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![Apache Spark](https://img.shields.io/badge/Apache-Spark-orange.svg)](https://spark.apache.org/)
[![Apache Hive](https://img.shields.io/badge/Apache-Hive-green.svg)](https://hive.apache.org/)
[![Scala](https://img.shields.io/badge/Scala-Programming-red.svg)](https://www.scala-lang.org/)
[![SQL](https://img.shields.io/badge/SQL-Queries-blue.svg)](https://hive.apache.org/)

> **Note: This repository is archived and no longer actively maintained.**

Big data processing examples using Apache Spark and Apache Hive for analyzing large datasets, demonstrating different approaches to data processing and analytics.

## 📁 Project Structure

- **[hive/](hive/)** - Apache Hive SQL examples
- **[spark/](spark/)** - Apache Spark Scala examples
- **[spectrum.sql](spectrum.sql)** - Redshift Spectrum examples

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **EMR Cluster**: Amazon EMR for running Spark and Hive
3. **S3 Bucket**: For data storage and processing
4. **Java/Scala**: For Spark development (optional)

### Setup

1. **Create EMR Cluster:**
   ```bash
   aws emr create-cluster \
       --name "BigDataBattle" \
       --release-label emr-6.x.0 \
       --applications Name=Spark Name=Hive \
       --ec2-attributes KeyName=your-key-pair \
       --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge \
       --instance-groups InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge
   ```

2. **Upload data to S3:**
   ```bash
   aws s3 cp your-data.csv s3://your-bucket/data/
   ```

## 🔧 Examples Covered

### Apache Hive
- **SQL-based data processing**: Traditional SQL queries on big data
- **Data warehousing**: Hive as a data warehouse solution
- **ETL processes**: Extract, transform, load operations
- **Performance optimization**: Query optimization techniques

### Apache Spark
- **Scala-based processing**: Programmatic data processing
- **In-memory computing**: Fast data processing with Spark
- **Machine learning**: MLlib integration
- **Stream processing**: Real-time data processing

### Redshift Spectrum
- **Serverless querying**: Query S3 data without managing clusters
- **SQL on S3**: Direct SQL queries on S3 data
- **Performance**: Optimized for large-scale queries

## 📚 Examples Overview

### Hive Examples
- **01countevents.sql**: Count events in dataset
- **02top10eventcategories.sql**: Top event categories analysis
- **03obamaeventsperyear.sql**: Temporal analysis of events
- **04obamaputinevents.sql**: Comparative event analysis
- **05obamaputineventslocal.sql**: Localized event analysis

### Spark Examples
- **00test.scala**: Basic Spark setup and testing
- **01countEvents.scala**: Event counting with Spark
- **02top10categories.scala**: Category analysis
- **03obamaEventsperYear.scala**: Temporal analysis
- **04obamaPutin.scala**: Comparative analysis
- **05obamaPutinLocal.scala**: Localized analysis

### Spectrum Examples
- **spectrum.sql**: Redshift Spectrum queries

## 🛠️ Running Examples

### Hive Queries
```bash
# Connect to EMR cluster
ssh -i your-key.pem hadoop@your-emr-master

# Run Hive queries
hive -f 01countevents.sql
```

### Spark Jobs
```bash
# Submit Spark job
spark-submit \
    --class CountEvents \
    --master yarn \
    01countEvents.scala
```

### Spectrum Queries
```bash
# Connect to Redshift
psql -h your-redshift-cluster -U username -d database -f spectrum.sql
```

## 📊 Data Processing Patterns

### Batch Processing
```sql
-- Hive batch processing
SELECT event_type, COUNT(*) as event_count
FROM events
WHERE event_date >= '2020-01-01'
GROUP BY event_type
ORDER BY event_count DESC;
```

### Real-time Processing
```scala
// Spark streaming
val stream = spark.readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092")
  .option("subscribe", "events")
  .load()
```

### Interactive Analysis
```sql
-- Spectrum interactive queries
SELECT *
FROM spectrum.events
WHERE event_date = CURRENT_DATE
LIMIT 100;
```

## ⚠️ Important Notes

- **Cluster Costs**: EMR clusters incur costs while running
- **Data Size**: Ensure sufficient storage for large datasets
- **Performance**: Monitor cluster performance and optimize
- **Security**: Configure proper security groups and IAM roles
- **Monitoring**: Use CloudWatch for cluster monitoring

## 🔗 Related Examples

- **[athena/](../athena/)** - Serverless querying alternatives
- **[ML/Spark/](../ML/Spark/)** - Machine learning with Spark
- **[serverlessPipeline/](../serverlessPipeline/)** - Real-time processing

## 📖 Documentation

- [Apache Spark Documentation](https://spark.apache.org/docs/)
- [Apache Hive Documentation](https://hive.apache.org/)
- [Amazon EMR Documentation](https://docs.aws.amazon.com/emr/)
- [Redshift Spectrum Documentation](https://docs.aws.amazon.com/redshift/)

## 🎯 Use Cases

### Data Analytics
- **Business intelligence**: Sales and customer analysis
- **Log analysis**: Application and system logs
- **Social media analysis**: Sentiment and trend analysis

### Machine Learning
- **Feature engineering**: Data preparation for ML
- **Model training**: Large-scale model training
- **Prediction serving**: Real-time predictions

### Data Engineering
- **ETL pipelines**: Data transformation workflows
- **Data quality**: Data validation and cleaning
- **Data governance**: Data lineage and cataloging

## 💡 Best Practices

- **Cluster Sizing**: Right-size clusters for workload
- **Data Partitioning**: Partition data for better performance
- **Caching**: Cache frequently accessed data
- **Monitoring**: Monitor job progress and performance
- **Cost Optimization**: Use spot instances when possible

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 