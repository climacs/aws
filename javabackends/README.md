# Java Backend Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![Java](https://img.shields.io/badge/Java-8+-orange.svg)](https://www.oracle.com/java/)
[![AWS SDK](https://img.shields.io/badge/AWS-SDK%20Java-blue.svg)](https://aws.amazon.com/sdk-for-java/)
[![Maven](https://img.shields.io/badge/Maven-Build-red.svg)](https://maven.apache.org/)

> **Note: This repository is archived and no longer actively maintained.**

Java backend examples demonstrating integration with various AWS services including DynamoDB, Redshift, Athena, Aurora, and Hive for building scalable backend applications.

## 📁 Project Structure

- **[AthenaSample.java](AthenaSample.java)** - Amazon Athena integration
- **[AuroraSample.java](AuroraSample.java)** - Amazon Aurora database integration
- **[Connect.java](Connect.java)** - AWS service connection utilities
- **[DynamoDBMovie.java](DynamoDBMovie.java)** - DynamoDB movie database example
- **[DynamoDBSample.java](DynamoDBSample.java)** - Basic DynamoDB operations
- **[DynamoDBSampleMapper.java](DynamoDBSampleMapper.java)** - DynamoDB mapper example
- **[HiveSample.java](HiveSample.java)** - Apache Hive integration
- **[Queries.java](Queries.java)** - Common database queries
- **[RedshiftSample.java](RedshiftSample.java)** - Amazon Redshift integration

## 🚀 Getting Started

### Prerequisites

1. **Java**: Java 8 or higher
2. **Maven**: Apache Maven for build management
3. **AWS Account**: AWS account with appropriate permissions
4. **AWS CLI**: Configured AWS credentials

### Setup

1. **Install Java and Maven:**
   ```bash
   # Install Java (Ubuntu/Debian)
   sudo apt-get install openjdk-8-jdk
   
   # Install Maven
   sudo apt-get install maven
   ```

2. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

3. **Build the project:**
   ```bash
   mvn clean compile
   ```

## 🔧 Examples Covered

### Database Services
- **DynamoDB**: NoSQL database operations and mapping
- **Aurora**: Relational database integration
- **Redshift**: Data warehouse operations
- **Hive**: Big data querying

### Analytics Services
- **Athena**: Serverless query service
- **Data Analysis**: Complex query examples
- **Performance Optimization**: Query optimization techniques

### Backend Patterns
- **Connection Management**: AWS service connections
- **Data Access Layer**: Database abstraction
- **Error Handling**: Robust error management
- **Configuration**: Environment-based configuration

## 📚 Examples Overview

### DynamoDB Examples
- **DynamoDBSample.java**: Basic CRUD operations
- **DynamoDBSampleMapper.java**: Object mapping with DynamoDB
- **DynamoDBMovie.java**: Movie database application

### Database Examples
- **AuroraSample.java**: Aurora MySQL/PostgreSQL integration
- **RedshiftSample.java**: Redshift data warehouse operations
- **HiveSample.java**: Hive query execution

### Analytics Examples
- **AthenaSample.java**: Athena query execution
- **Queries.java**: Common analytical queries
- **Connect.java**: Service connection utilities

## 🛠️ Running Examples

### Basic DynamoDB Operations
```bash
# Compile and run
mvn compile exec:java -Dexec.mainClass="DynamoDBSample"
```

### Movie Database Example
```bash
mvn compile exec:java -Dexec.mainClass="DynamoDBMovie"
```

### Athena Query Execution
```bash
mvn compile exec:java -Dexec.mainClass="AthenaSample"
```

### Redshift Operations
```bash
mvn compile exec:java -Dexec.mainClass="RedshiftSample"
```

## 🔌 Code Examples

### DynamoDB Operations
```java
// Basic DynamoDB operations
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
    .withRegion(Regions.US_EAST_1)
    .build();

DynamoDB dynamoDB = new DynamoDB(client);
Table table = dynamoDB.getTable("Movies");

// Put item
Item item = new Item()
    .withPrimaryKey("year", 2015, "title", "The Big New Movie")
    .withString("info", "Nothing happens at all.");
table.putItem(item);
```

### Aurora Connection
```java
// Aurora database connection
String url = "jdbc:mysql://your-aurora-cluster:3306/database";
Properties props = new Properties();
props.setProperty("user", "username");
props.setProperty("password", "password");

try (Connection conn = DriverManager.getConnection(url, props)) {
    // Database operations
}
```

### Athena Query
```java
// Athena query execution
AmazonAthena athenaClient = AmazonAthenaClientBuilder.standard()
    .withRegion(Regions.US_EAST_1)
    .build();

StartQueryExecutionRequest startQueryExecutionRequest = new StartQueryExecutionRequest()
    .withQueryString("SELECT * FROM database.table LIMIT 10")
    .withResultConfiguration(new ResultConfiguration()
        .withOutputLocation("s3://your-bucket/athena-results/"));
```

## ⚠️ Important Notes

- **Dependencies**: Ensure all AWS SDK dependencies are included
- **Credentials**: Configure proper AWS credentials and permissions
- **Regions**: Set appropriate AWS regions for your services
- **Costs**: Monitor AWS service usage and costs
- **Security**: Implement proper security measures

## 🔗 Related Examples

- **[athena/](../athena/)** - Athena SQL examples
- **[bigdatabattle/](../bigdatabattle/)** - Big data processing
- **[lambda_frameworks/](../lambda_frameworks/)** - Serverless Java

## 📖 Documentation

- [AWS SDK for Java Documentation](https://docs.aws.amazon.com/sdk-for-java/)
- [DynamoDB Java API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/JavaDocumentAPI.html)
- [Aurora Documentation](https://docs.aws.amazon.com/aurora/)
- [Redshift Documentation](https://docs.aws.amazon.com/redshift/)

## 🎯 Use Cases

### Web Applications
- **User management**: User data storage and retrieval
- **Content management**: Content storage and delivery
- **E-commerce**: Product catalog and order management

### Data Analytics
- **Business intelligence**: Data analysis and reporting
- **Real-time analytics**: Live data processing
- **Data warehousing**: Large-scale data storage

### Backend Services
- **API backends**: RESTful service implementations
- **Microservices**: Service-oriented architecture
- **Data processing**: ETL and data transformation

## 💡 Best Practices

- **Connection Pooling**: Use connection pools for database connections
- **Error Handling**: Implement comprehensive error handling
- **Logging**: Add proper logging for debugging and monitoring
- **Configuration**: Use external configuration files
- **Testing**: Write unit and integration tests

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 