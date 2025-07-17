# Amazon Redshift Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS Redshift](https://img.shields.io/badge/AWS-Redshift-orange.svg)](https://aws.amazon.com/redshift/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Compatible-blue.svg)](https://www.postgresql.org/)
[![SQL](https://img.shields.io/badge/SQL-Queries-green.svg)](https://docs.aws.amazon.com/redshift/)

> **Note: This repository is archived and no longer actively maintained.**

Amazon Redshift examples and database operations demonstrating data warehousing, analytics, and SQL query optimization for large-scale data processing.

## 📁 Project Structure

- **[psqlRedshift.sh](psqlRedshift.sh)** - PostgreSQL client connection script

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **Redshift Cluster**: Amazon Redshift cluster running
3. **PostgreSQL Client**: psql command-line tool
4. **Network Access**: VPC and security group configuration

### Setup

1. **Install PostgreSQL client:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install postgresql-client
   
   # macOS
   brew install postgresql
   ```

2. **Configure Redshift cluster:**
   ```bash
   # Create Redshift cluster via AWS CLI
   aws redshift create-cluster \
       --cluster-identifier my-redshift-cluster \
       --node-type dc2.large \
       --master-username admin \
       --master-user-password your-password \
       --cluster-type single-node
   ```

3. **Configure security groups:**
   - Allow inbound connections on port 5439
   - Configure VPC and subnet settings

## 🔧 Examples Covered

### Database Operations
- **Connection management**: Secure database connections
- **Query execution**: SQL query processing
- **Data loading**: Bulk data import operations
- **Performance optimization**: Query and cluster optimization

### Analytics Features
- **Columnar storage**: Optimized for analytical queries
- **Massive parallel processing**: Distributed query execution
- **Compression**: Data compression for storage efficiency
- **Sorting and distribution**: Data organization strategies

### Integration Examples
- **S3 integration**: Loading data from S3
- **ETL processes**: Extract, transform, load workflows
- **Data warehousing**: Large-scale data storage
- **Business intelligence**: Analytics and reporting

## 📚 Examples Overview

### Connection Script
- **psqlRedshift.sh**: PostgreSQL client connection to Redshift
- **Connection parameters**: Host, port, database, credentials
- **SSL configuration**: Secure connection setup
- **Environment variables**: Configuration management

## 🛠️ Running Examples

### Connect to Redshift
```bash
# Make script executable
chmod +x psqlRedshift.sh

# Connect to Redshift cluster
./psqlRedshift.sh
```

### Basic SQL Operations
```sql
-- Create table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_date TIMESTAMP
);

-- Load data from S3
COPY users FROM 's3://your-bucket/users.csv'
CREDENTIALS 'aws_access_key_id=YOUR_KEY;aws_secret_access_key=YOUR_SECRET'
CSV;

-- Query data
SELECT username, COUNT(*) as user_count
FROM users
GROUP BY username
ORDER BY user_count DESC;
```

## 🔌 Connection Examples

### Direct Connection
```bash
# Connect using psql
psql -h your-redshift-cluster.region.redshift.amazonaws.com \
     -p 5439 \
     -U admin \
     -d dev
```

### Connection String
```bash
# Connection string format
postgresql://username:password@host:port/database
```

### SSL Connection
```bash
# SSL-enabled connection
psql "sslmode=require host=your-cluster port=5439 dbname=dev user=admin"
```

## ⚠️ Important Notes

- **Costs**: Redshift clusters incur costs while running
- **Performance**: Monitor query performance and cluster metrics
- **Security**: Use SSL connections and proper authentication
- **Scaling**: Consider cluster scaling for performance needs
- **Backup**: Configure automated backups and snapshots

## 🔗 Related Examples

- **[athena/](../athena/)** - Serverless querying alternatives
- **[javabackends/](../javabackends/)** - Java Redshift integration
- **[bigdatabattle/](../bigdatabattle/)** - Big data processing

## 📖 Documentation

- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/)
- [Redshift SQL Reference](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_sql.html)
- [Redshift Best Practices](https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🎯 Use Cases

### Data Warehousing
- **Business intelligence**: Sales and customer analytics
- **Financial reporting**: Revenue and expense analysis
- **Operational analytics**: Performance and efficiency metrics

### Analytics
- **Customer analytics**: Behavior and segmentation analysis
- **Product analytics**: Usage and performance metrics
- **Market analysis**: Competitive and trend analysis

### Reporting
- **Executive dashboards**: High-level business metrics
- **Operational reports**: Daily and weekly reports
- **Ad-hoc analysis**: Exploratory data analysis

## 💡 Best Practices

### Performance Optimization
- **Distribution keys**: Choose appropriate distribution keys
- **Sort keys**: Use sort keys for query optimization
- **Compression**: Apply compression to reduce storage
- **VACUUM**: Regular table maintenance

### Data Loading
- **COPY command**: Use COPY for bulk data loading
- **S3 integration**: Load data directly from S3
- **Parallel loading**: Use multiple COPY commands
- **Data validation**: Validate data before loading

### Query Optimization
- **EXPLAIN**: Use EXPLAIN to analyze query plans
- **Indexing**: Create appropriate indexes
- **Partitioning**: Use table partitioning for large tables
- **Monitoring**: Monitor query performance

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 