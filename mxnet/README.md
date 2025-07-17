# Apache MXNet Deep Learning Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![Apache MXNet](https://img.shields.io/badge/Apache-MXNet-blue.svg)](https://mxnet.apache.org/)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Python-green.svg)](https://mxnet.apache.org/)
[![GPU](https://img.shields.io/badge/GPU-Support-red.svg)](https://mxnet.apache.org/get_started/install.html)

> **Note: This repository is archived and no longer actively maintained.**

Comprehensive deep learning examples using Apache MXNet framework, covering image classification, object detection, and neural network training on various datasets.

## 📁 Project Structure

- **[bench.py](bench.py)** - Performance benchmarking script
- **[cifar/](cifar/)** - CIFAR-10 image classification examples
- **[imagenet/](imagenet/)** - ImageNet dataset examples
- **[intro/](intro/)** - Introduction to MXNet examples
- **[keras/](keras/)** - Keras integration examples
- **[mnist/](mnist/)** - MNIST digit recognition examples
- **[raspberrypi/](raspberrypi/)** - Raspberry Pi deployment examples

## 🚀 Getting Started

### Prerequisites

1. **Python**: Python 3.7 or higher
2. **MXNet**: Install MXNet with GPU support (optional)
3. **CUDA**: For GPU acceleration (optional)
4. **Dependencies**: Install required packages

### Setup

1. **Install MXNet:**
   ```bash
   # CPU version
   pip install mxnet
   
   # GPU version (CUDA 11.x)
   pip install mxnet-cu110
   ```

2. **Install additional dependencies:**
   ```bash
   pip install numpy matplotlib pillow requests
   ```

3. **Download datasets:**
   ```bash
   cd mxnet/mnist/
   ./download_mnist.sh
   
   cd ../cifar/
   ./download_cifar10.sh
   ```

## 🔧 Examples Covered

### MNIST Digit Recognition
- **Basic neural network training**
- **Convolutional neural networks (CNN)**
- **Model prediction and evaluation**
- **Data preprocessing and augmentation**

### CIFAR-10 Image Classification
- **ResNet architecture implementation**
- **Transfer learning examples**
- **Learning rate scheduling**
- **Model fine-tuning**

### ImageNet Examples
- **Large-scale image classification**
- **Pre-trained model usage**
- **Validation set preparation**
- **Performance optimization**

### Raspberry Pi Deployment
- **Edge computing examples**
- **Model optimization for mobile**
- **Real-time inference**
- **Camera integration**

## 📚 Examples Overview

### MNIST Examples
- **trainModel.py**: Basic neural network training
- **trainModelv2.py**: Improved training with data augmentation
- **trainModelv3.py**: Advanced training with callbacks
- **predict.py**: Model prediction and evaluation
- **extractData.py**: Data preprocessing utilities

### CIFAR-10 Examples
- **trainLeNet.py**: LeNet architecture for CIFAR-10
- **trainResnextFixedlr.py**: ResNeXt with fixed learning rate
- **trainResnextVariablelr.py**: ResNeXt with variable learning rate
- **finetuneResnext.py**: Transfer learning examples
- **finetuneResnextAdadelta.py**: Adadelta optimizer examples

### Introduction Examples
- **firstexample.py**: Basic MXNet introduction
- **inception.py**: Inception model usage
- **compare.py**: Model comparison utilities
- **splitRGBImage.py**: Image processing utilities

### Raspberry Pi Examples
- **camera/**: Camera integration and real-time inference
- **inception_predict.py**: Pre-trained model inference
- **PollyApi.py**: Text-to-speech integration

## 🛠️ Running Examples

### Basic Training
```bash
cd mxnet/mnist/
python trainModel.py
```

### CIFAR-10 Training
```bash
cd mxnet/cifar/
python trainLeNet.py
```

### Model Prediction
```bash
cd mxnet/mnist/
python predict.py
```

### Performance Benchmarking
```bash
cd mxnet/
python bench.py
```

## 🎯 Key Features

### Model Architectures
- **LeNet**: Basic CNN for digit recognition
- **ResNeXt**: Advanced CNN for image classification
- **Inception**: Pre-trained models for transfer learning
- **Custom Networks**: Flexible architecture design

### Training Features
- **Data Augmentation**: Image rotation, scaling, and noise
- **Learning Rate Scheduling**: Adaptive learning rates
- **Transfer Learning**: Pre-trained model fine-tuning
- **Multi-GPU Training**: Distributed training support

### Deployment Features
- **Model Export**: Save models for inference
- **Edge Deployment**: Raspberry Pi optimization
- **Real-time Inference**: Camera integration
- **API Integration**: AWS services integration

## ⚠️ Important Notes

- **GPU Memory**: Large models may require significant GPU memory
- **Dataset Size**: ImageNet requires substantial storage space
- **Training Time**: Deep learning training can take hours or days
- **CUDA Version**: Ensure MXNet version matches your CUDA version
- **Dependencies**: Some examples may use older library versions

## 🔗 Related Examples

- **[ML/](../ML/)** - Traditional machine learning examples
- **[AmazonAI/](../AmazonAI/)** - AWS AI service integration
- **[iot/](../iot/)** - IoT and edge computing examples

## 📖 Documentation

- [Apache MXNet Documentation](https://mxnet.apache.org/)
- [MXNet Tutorials](https://mxnet.apache.org/tutorials/)
- [MXNet API Reference](https://mxnet.apache.org/api/python/)
- [MXNet Installation Guide](https://mxnet.apache.org/get_started/install.html)

## 🎓 Learning Path

1. **Beginner**: Start with `intro/firstexample.py`
2. **Intermediate**: Work with MNIST examples
3. **Advanced**: Train on CIFAR-10 dataset
4. **Expert**: Deploy to edge devices

## 💡 Tips

- **Start with CPU**: Use CPU version for initial learning
- **Monitor GPU**: Use `nvidia-smi` to monitor GPU usage
- **Save Checkpoints**: Regularly save model checkpoints
- **Use Validation**: Always validate on separate dataset
- **Optimize Data**: Use data loading optimization techniques

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained


