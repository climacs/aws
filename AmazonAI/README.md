# Amazon AI Services Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS AI](https://img.shields.io/badge/AWS-AI%20Services-orange.svg)](https://aws.amazon.com/ai/)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)

> **Note: This repository is archived and no longer actively maintained.**

Examples and experiments with Amazon AI services including Amazon Polly, Amazon Rekognition, Amazon Comprehend, and Amazon Translate.

## 📁 Project Structure

- **[billboard/](billboard/)** - Billboard text detection and translation using Rekognition and Translate
- **[polly/](polly/)** - Text-to-speech examples using Amazon Polly
- **[rekognition/](rekognition/)** - Image and video analysis using Amazon Rekognition
- **[rekognitionvideo/](rekognitionvideo/)** - Video analysis examples
- **[transcribe/](transcribe/)** - Speech-to-text examples using Amazon Transcribe
- **[translate/](translate/)** - Text translation examples using Amazon Translate

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Python**: Python 3.7 or higher
4. **Dependencies**: Install required packages for each example

### Setup

1. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

2. **Install dependencies for specific examples:**
   ```bash
   cd AmazonAI/[example-folder]
   pip install -r requirements.txt
   ```

## 🔧 Services Covered

### Amazon Polly
- Text-to-speech conversion
- SSML (Speech Synthesis Markup Language) examples
- Multiple voice options

### Amazon Rekognition
- Image analysis and object detection
- Face detection and comparison
- Text detection in images
- Video analysis

### Amazon Comprehend
- Natural language processing
- Sentiment analysis
- Entity recognition
- Key phrase extraction

### Amazon Translate
- Text translation between languages
- Batch translation
- Real-time translation

## 📚 Examples Overview

### Billboard Example
The `billboard/` folder contains a complete example that:
- Detects text in images using Rekognition
- Translates detected text using Translate
- Converts text to speech using Polly
- Demonstrates end-to-end AI workflow

### Polly Examples
- Basic text-to-speech conversion
- SSML markup for enhanced speech
- Different voice and language options

### Rekognition Examples
- Face detection and analysis
- Object and scene detection
- Text detection in images
- Face comparison and recognition

### Translation Examples
- Text translation between multiple languages
- C++ examples for translation
- Batch processing capabilities

## ⚠️ Important Notes

- **AWS Credentials**: Ensure you have proper AWS credentials configured
- **Service Limits**: Be aware of AWS service limits and pricing
- **Permissions**: Ensure your AWS user/role has appropriate permissions for AI services
- **SDK Versions**: Examples may use older AWS SDK versions

## 📖 Documentation

- [Amazon Polly Documentation](https://docs.aws.amazon.com/polly/)
- [Amazon Rekognition Documentation](https://docs.aws.amazon.com/rekognition/)
- [Amazon Comprehend Documentation](https://docs.aws.amazon.com/comprehend/)
- [Amazon Translate Documentation](https://docs.aws.amazon.com/translate/)

## 🔗 Related Examples

- **[ML/](../ML/)** - Machine learning examples
- **[lambda_frameworks/](../lambda_frameworks/)** - Serverless AI integration
- **[iot/](../iot/)** - IoT with AI services

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 