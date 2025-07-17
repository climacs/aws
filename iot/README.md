# AWS IoT Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS IoT](https://img.shields.io/badge/AWS-IoT-orange.svg)](https://aws.amazon.com/iot/)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![MQTT](https://img.shields.io/badge/MQTT-Protocol-green.svg)](https://mqtt.org/)

> **Note: This repository is archived and no longer actively maintained.**

AWS IoT examples and implementations covering device connectivity, message processing, and IoT application development using AWS IoT Core and related services.

## 📁 Project Structure

- **[python/](python/)** - Python-based IoT examples
  - **[helloWorld.py](python/helloWorld.py)** - Basic IoT device connection
  - **[lambda/](python/lambda/)** - IoT Lambda function examples
  - **[server/](python/server/)** - IoT server and camera integration

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Python**: Python 3.7 or higher
4. **IoT Device**: Raspberry Pi or similar device (optional)
5. **Camera**: For computer vision examples (optional)

### Setup

1. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

2. **Install Python dependencies:**
   ```bash
   cd iot/python/
   pip install boto3 paho-mqtt opencv-python numpy
   ```

3. **Create IoT Thing and certificates:**
   ```bash
   # Create IoT thing
   aws iot create-thing --thing-name my-iot-device
   
   # Create certificates
   aws iot create-keys-and-certificate --set-as-active
   ```

## 🔧 Examples Covered

### Basic IoT Connectivity
- **Device registration**: Creating IoT things and certificates
- **MQTT communication**: Publishing and subscribing to topics
- **Message processing**: Handling device messages
- **Security**: Certificate-based authentication

### Lambda Integration
- **Message processing**: Lambda functions for IoT data
- **Event handling**: Responding to device events
- **Data transformation**: Processing IoT messages
- **Integration**: Connecting IoT with other AWS services

### Computer Vision Integration
- **Camera integration**: Real-time image capture
- **Image processing**: OpenCV-based image analysis
- **ML inference**: Running ML models on device
- **Edge computing**: Local processing capabilities

## 📚 Examples Overview

### Basic IoT Examples
- **helloWorld.py**: Simple IoT device connection and messaging
- **iot_connect.py**: Advanced connection management
- **iot_topics.py**: Topic management and message routing

### Lambda Examples
- **lambda.py**: IoT message processing Lambda function
- **Event handling**: Processing device events and data

### Server Examples
- **server.py**: IoT server implementation
- **camera.py**: Camera integration and image capture
- **inception_predict.py**: ML model inference
- **download.sh**: Model download script

## 🛠️ Running Examples

### Basic IoT Device
```bash
cd iot/python/
python helloWorld.py
```

### IoT Server
```bash
cd iot/python/server/
python server.py
```

### Camera Integration
```bash
cd iot/python/server/
python camera.py
```

### Lambda Function
```bash
# Deploy Lambda function
cd iot/python/lambda/
# Use AWS CLI or console to deploy lambda.py
```

## 🔌 IoT Architecture

### Device to Cloud
```
IoT Device → AWS IoT Core → Lambda → Other AWS Services
```

### Cloud to Device
```
AWS Services → Lambda → AWS IoT Core → IoT Device
```

### Edge Processing
```
IoT Device → Local Processing → AWS IoT Core → Cloud
```

## 📡 MQTT Topics

### Common Topic Patterns
- **Device data**: `devices/{device-id}/data`
- **Device status**: `devices/{device-id}/status`
- **Commands**: `devices/{device-id}/commands`
- **Configuration**: `devices/{device-id}/config`

### Example Topics
```python
# Publishing device data
client.publish("devices/raspberry-pi/temperature", "23.5")

# Subscribing to commands
client.subscribe("devices/raspberry-pi/commands")
```

## ⚠️ Important Notes

- **Security**: Always use certificates for device authentication
- **Topics**: Use hierarchical topic structure for organization
- **QoS**: Choose appropriate Quality of Service levels
- **Limits**: Be aware of AWS IoT limits and quotas
- **Costs**: Monitor IoT message and device costs

## 🔗 Related Examples

- **[mxnet/raspberrypi/](../mxnet/raspberrypi/)** - Edge ML examples
- **[lambda_frameworks/](../lambda_frameworks/)** - IoT Lambda functions
- **[AmazonAI/](../AmazonAI/)** - AI service integration

## 📖 Documentation

- [AWS IoT Documentation](https://docs.aws.amazon.com/iot/)
- [AWS IoT Core Guide](https://docs.aws.amazon.com/iot/latest/developerguide/)
- [MQTT Protocol](https://mqtt.org/)
- [AWS IoT SDK for Python](https://github.com/aws/aws-iot-device-sdk-python)

## 🎯 Use Cases

### Smart Home
- **Temperature monitoring**: Real-time temperature data
- **Security cameras**: Motion detection and alerts
- **Smart appliances**: Device control and monitoring

### Industrial IoT
- **Sensor networks**: Environmental monitoring
- **Predictive maintenance**: Equipment health monitoring
- **Quality control**: Production line monitoring

### Agriculture
- **Soil monitoring**: Moisture and nutrient levels
- **Weather stations**: Environmental data collection
- **Irrigation control**: Automated watering systems

## 💡 Best Practices

- **Security First**: Use certificates and proper authentication
- **Topic Design**: Plan your MQTT topic hierarchy
- **Error Handling**: Implement robust error handling
- **Monitoring**: Monitor device connectivity and performance
- **Scalability**: Design for large numbers of devices

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 