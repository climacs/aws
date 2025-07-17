# Amazon Athena Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS Athena](https://img.shields.io/badge/AWS-Athena-orange.svg)](https://aws.amazon.com/athena/)
[![SQL](https://img.shields.io/badge/SQL-Queries-blue.svg)](https://docs.aws.amazon.com/athena/)
[![Hive](https://img.shields.io/badge/Apache-Hive-green.svg)](https://hive.apache.org/)

> **Note: This repository is archived and no longer actively maintained.**

Amazon Athena examples and SQL queries for interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.

## 📁 Project Structure

- **[gdelt/](gdelt/)** - GDELT (Global Database of Events, Language, and Tone) dataset examples
- **[sales/](sales/)** - Sales data analysis examples

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **S3 Bucket**: Data must be stored in S3
4. **Athena Workgroup**: Configure Athena workgroup for query execution

### Setup

1. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

2. **Create S3 bucket for Athena results:**
   ```bash
   aws s3 mb s3://your-athena-results-bucket
   ```

3. **Configure Athena workgroup:**
   - Go to AWS Athena console
   - Create or use default workgroup
   - Set output location to your S3 bucket

## 🔧 Examples Covered

### GDELT Dataset Analysis
The `gdelt/` folder contains examples for analyzing the GDELT dataset:
- **Event data analysis**: Global events and their relationships
- **Country and region analysis**: Geographic event distribution
- **Temporal analysis**: Events over time
- **Entity and actor analysis**: People, organizations, and locations

### Sales Data Analysis
The `sales/` folder contains examples for sales data analysis:
- **Data format optimization**: CSV, Parquet, ORC comparisons
- **Performance optimization**: Compression and partitioning
- **Query optimization**: Best practices for Athena queries

## 📚 Examples Overview

### GDELT Examples
- **create_tables.txt**: Table creation scripts for GDELT data
- **sql_queries.txt**: Sample queries for event analysis
- **countries.txt**: Country code reference data
- **eventcodes.txt**: Event code definitions
- **ethnic.txt**: Ethnic group codes
- **groups.txt**: Group type codes
- **religion.txt**: Religion codes
- **types.txt**: Event type codes

### Sales Examples
- **create_table_csv.txt**: CSV table creation
- **create_table_parquet.txt**: Parquet table creation
- **create_table_orc.txt**: ORC table creation
- **sql_queries.txt**: Sales analysis queries
- **csv-to-column.q**: CSV to columnar format conversion

## 🛠️ Running Queries

### Using AWS CLI
```bash
# Execute a query
aws athena start-query-execution \
    --query-string "SELECT * FROM your_database.your_table LIMIT 10" \
    --result-configuration OutputLocation=s3://your-results-bucket/
```

### Using AWS Console
1. Go to AWS Athena console
2. Select your database
3. Paste query from example files
4. Click "Run query"

### Using JDBC/ODBC
```bash
# For Java applications
cd ../javabackends/
# Use AthenaSample.java
```

## 📊 Data Formats Supported

- **CSV**: Comma-separated values
- **JSON**: JavaScript Object Notation
- **Parquet**: Columnar storage format
- **ORC**: Optimized Row Columnar format
- **Avro**: Data serialization format

## ⚡ Performance Optimization

### Best Practices
1. **Use columnar formats**: Parquet or ORC for better performance
2. **Partition data**: Partition by date, region, or other dimensions
3. **Compress data**: Use compression to reduce storage and query costs
4. **Limit columns**: Only select needed columns
5. **Use appropriate file sizes**: 128MB to 1GB per file

### Example Optimizations
```sql
-- Partitioned table creation
CREATE EXTERNAL TABLE events_partitioned (
    event_id STRING,
    event_date STRING,
    event_type STRING
)
PARTITIONED BY (year STRING, month STRING)
STORED AS PARQUET
LOCATION 's3://your-bucket/events/';
```

## ⚠️ Important Notes

- **Cost**: Athena charges per TB of data scanned
- **Data Location**: All data must be in S3
- **Query Limits**: Maximum query execution time is 30 minutes
- **Concurrent Queries**: Limited by your account limits
- **Data Formats**: Ensure data is in supported formats

## 🔗 Related Examples

- **[javabackends/](../javabackends/)** - Java Athena integration
- **[bigdatabattle/](../bigdatabattle/)** - Big data processing examples
- **[redshift/](../redshift/)** - Data warehouse alternatives

## 📖 Documentation

- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/)
- [Athena SQL Reference](https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html)
- [GDELT Project](https://www.gdeltproject.org/)
- [Athena Best Practices](https://docs.aws.amazon.com/athena/latest/ug/best-practices.html)

## 💡 Tips

- **Start small**: Test queries on small datasets first
- **Monitor costs**: Use AWS Cost Explorer to track Athena usage
- **Optimize storage**: Convert data to columnar formats
- **Use partitions**: Partition data for faster queries
- **Cache results**: Use query result caching when possible

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 