# AWS Edge Computing Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![Lambda@Edge](https://img.shields.io/badge/Lambda%40Edge-Edge%20Computing-orange.svg)](https://aws.amazon.com/lambda/edge/)
[![CloudFront](https://img.shields.io/badge/AWS-CloudFront-blue.svg)](https://aws.amazon.com/cloudfront/)
[![JavaScript](https://img.shields.io/badge/JavaScript-Node.js-yellow.svg)](https://nodejs.org/)

> **Note: This repository is archived and no longer actively maintained.**

AWS Edge Computing examples demonstrating Lambda@Edge functions and CloudFront integration for processing requests at the edge, closer to end users for improved performance and reduced latency.

## 📁 Project Structure

- **[index.html](index.html)** - Sample web page for edge processing
- **[lambda.js](lambda.js)** - Lambda@Edge function examples

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Node.js**: For Lambda@Edge function development
4. **CloudFront Distribution**: For edge function deployment

### Setup

1. **Install Node.js dependencies:**
   ```bash
   npm init -y
   npm install aws-sdk
   ```

2. **Create S3 bucket for static content:**
   ```bash
   aws s3 mb s3://your-edge-bucket
   aws s3 website s3://your-edge-bucket --index-document index.html
   ```

3. **Upload static content:**
   ```bash
   aws s3 cp index.html s3://your-edge-bucket/
   ```

## 🔧 Examples Covered

### Lambda@Edge Functions
- **Request processing**: Intercept and modify incoming requests
- **Response processing**: Modify responses before delivery
- **Authentication**: Edge-based authentication and authorization
- **Content optimization**: Dynamic content optimization

### CloudFront Integration
- **Distribution setup**: CloudFront distribution configuration
- **Cache behavior**: Custom cache behaviors and policies
- **Origin configuration**: S3 and custom origin setup
- **Security**: HTTPS and security headers

### Edge Processing
- **A/B testing**: Edge-based A/B testing
- **Geolocation**: Location-based content delivery
- **Device detection**: Device-specific content optimization
- **Performance monitoring**: Edge performance metrics

## 📚 Examples Overview

### Static Content
- **index.html**: Sample web page for edge processing
- **Content delivery**: Static content served via CloudFront

### Lambda Functions
- **lambda.js**: Lambda@Edge function implementations
- **Request handling**: Request interception and modification
- **Response processing**: Response optimization and modification

## 🛠️ Running Examples

### Deploy Lambda@Edge Function
```bash
# Package Lambda function
zip -r lambda-edge.zip lambda.js

# Create Lambda function
aws lambda create-function \
    --function-name edge-function \
    --runtime nodejs14.x \
    --role arn:aws:iam::account:role/lambda-edge-role \
    --handler lambda.handler \
    --zip-file fileb://lambda-edge.zip
```

### Create CloudFront Distribution
```bash
# Create CloudFront distribution
aws cloudfront create-distribution \
    --distribution-config file://distribution-config.json
```

### Test Edge Function
```bash
# Access your CloudFront distribution
curl https://your-distribution.cloudfront.net/
```

## 🔌 Lambda@Edge Examples

### Request Processing
```javascript
// Viewer request event
exports.handler = async (event) => {
    const request = event.Records[0].cf.request;
    
    // Add custom headers
    request.headers['x-custom-header'] = [{
        key: 'x-custom-header',
        value: 'edge-processed'
    }];
    
    return request;
};
```

### Response Processing
```javascript
// Viewer response event
exports.handler = async (event) => {
    const response = event.Records[0].cf.response;
    
    // Add security headers
    response.headers['x-frame-options'] = [{
        key: 'x-frame-options',
        value: 'DENY'
    }];
    
    return response;
};
```

### A/B Testing
```javascript
// A/B testing at the edge
exports.handler = async (event) => {
    const request = event.Records[0].cf.request;
    const userAgent = request.headers['user-agent'][0].value;
    
    // Simple A/B test based on user agent
    if (userAgent.includes('Mobile')) {
        request.uri = '/mobile' + request.uri;
    }
    
    return request;
};
```

## ⚠️ Important Notes

- **Function Limits**: Lambda@Edge has specific limitations
- **Cold Starts**: Functions may experience cold starts
- **Costs**: Monitor Lambda@Edge execution costs
- **Deployment**: Functions are replicated to edge locations
- **Debugging**: Edge function debugging can be challenging

## 🔗 Related Examples

- **[lambda_frameworks/](../lambda_frameworks/)** - Lambda function examples
- **[CF/](../CF/)** - CloudFormation for edge infrastructure
- **[iot/](../iot/)** - Edge IoT processing

## 📖 Documentation

- [Lambda@Edge Documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html)
- [CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [Lambda@Edge Programming Model](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-programming-model.html)
- [Edge Function Examples](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html)

## 🎯 Use Cases

### Content Delivery
- **Dynamic content**: Personalized content delivery
- **Image optimization**: On-the-fly image processing
- **Video streaming**: Adaptive bitrate streaming
- **Static assets**: Optimized static file delivery

### Security
- **Bot protection**: Edge-based bot detection
- **DDoS protection**: Distributed denial-of-service protection
- **Authentication**: Edge-based user authentication
- **Rate limiting**: Request rate limiting

### Performance
- **Caching**: Intelligent content caching
- **Compression**: Dynamic content compression
- **Minification**: CSS/JS minification
- **Optimization**: Performance optimization

## 💡 Best Practices

### Function Design
- **Keep functions small**: Minimize function size and complexity
- **Optimize cold starts**: Reduce initialization time
- **Error handling**: Implement robust error handling
- **Monitoring**: Use CloudWatch for monitoring

### Performance
- **Cache effectively**: Use CloudFront caching
- **Minimize processing**: Keep edge processing lightweight
- **Optimize code**: Use efficient algorithms and data structures
- **Monitor costs**: Track Lambda@Edge execution costs

### Security
- **Input validation**: Validate all inputs
- **Output sanitization**: Sanitize outputs
- **Access control**: Implement proper access controls
- **HTTPS**: Always use HTTPS

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 