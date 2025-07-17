# AWS Lambda Frameworks & Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/lambda/)
[![Serverless](https://img.shields.io/badge/Serverless-Framework-yellow.svg)](https://serverless.com/)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/node.js-12+-green.svg)](https://nodejs.org/)

> **Note: This repository is archived and no longer actively maintained.**

Comprehensive examples of AWS Lambda functions using various frameworks and deployment methods including Serverless Framework, Chalice, SAM, and Gordon.

## 📁 Project Structure

### Frameworks
- **[chalice/](chalice/)** - AWS Chalice framework examples
- **[serverless/](serverless/)** - Serverless Framework examples
- **[sam/](sam/)** - AWS SAM (Serverless Application Model) examples
- **[gordon/](gordon/)** - Gordon framework examples

### Basic Lambda Examples
- **[firstlambda/](firstlambda/)** - Basic Lambda function with manual deployment
- **[secondlambda/](secondlambda/)** - Advanced Lambda with CloudFormation

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Node.js**: For Serverless Framework and SAM
4. **Python**: For Chalice and Python Lambda functions
5. **Docker**: For SAM local testing (optional)

### Setup

1. **Install frameworks:**
   ```bash
   # Serverless Framework
   npm install -g serverless
   
   # AWS SAM CLI
   pip install aws-sam-cli
   
   # AWS Chalice
   pip install chalice
   ```

2. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

## 🔧 Frameworks Covered

### AWS Chalice
- Python-based serverless framework
- Automatic API Gateway integration
- Built-in deployment tools
- Examples: Hello World, Image Predictor, Image Resizer

### Serverless Framework
- Multi-language support
- Plugin ecosystem
- Infrastructure as code
- Examples: Hello World, API endpoints, SageMaker integration

### AWS SAM
- AWS-native serverless framework
- CloudFormation-based deployment
- Local testing capabilities
- Examples: Basic Lambda functions

### Gordon
- Lightweight serverless framework
- Simple configuration
- Examples: Hello World functions

## 📚 Examples Overview

### Chalice Examples
- **helloworld/**: Basic API endpoint
- **predictor/**: ML model prediction endpoint
- **resizer/**: Image resizing service
- **s3test/**: S3 integration example
- **sagemakertrainer/**: SageMaker training integration

### Serverless Examples
- **hello/**: Basic Lambda function
- **helloapi/**: API Gateway integration
- **addIntegersAPI/**: Simple API with parameters
- **addIntegersStandalone/**: Standalone function
- **sagemakerscheduler/**: SageMaker scheduling

### Basic Lambda Examples
- **firstlambda/**: Manual deployment scripts
- **secondlambda/**: CloudFormation deployment

## 🛠️ Deployment Methods

### Manual Deployment
```bash
cd firstlambda/
./deploy.sh
```

### Serverless Framework
```bash
cd serverless/hello/
serverless deploy
```

### AWS Chalice
```bash
cd chalice/helloworld/
chalice deploy
```

### AWS SAM
```bash
cd sam/firstdemo/
sam build
sam deploy
```

## 📖 Key Features

- **Multiple Languages**: Python, Node.js, Java examples
- **Various Integrations**: API Gateway, S3, SageMaker, DynamoDB
- **Different Complexity Levels**: From basic hello world to complex ML pipelines
- **Deployment Scripts**: Automated deployment and cleanup scripts

## ⚠️ Important Notes

- **AWS Credentials**: Ensure proper AWS credentials are configured
- **Service Limits**: Be aware of Lambda limits and pricing
- **Permissions**: Ensure appropriate IAM roles and policies
- **SDK Versions**: Examples may use older AWS SDK versions
- **Framework Versions**: Some examples may use older framework versions

## 🔗 Related Examples

- **[AmazonAI/](../AmazonAI/)** - AI service integration with Lambda
- **[serverlessPipeline/](../serverlessPipeline/)** - Complex serverless architectures
- **[iot/](../iot/)** - IoT Lambda functions

## 📖 Documentation

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Serverless Framework Documentation](https://serverless.com/framework/docs/)
- [AWS Chalice Documentation](https://aws.github.io/chalice/)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 