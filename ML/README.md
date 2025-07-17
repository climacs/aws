# Machine Learning Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Python-blue.svg)](https://scikit-learn.org/)
[![Apache Spark](https://img.shields.io/badge/Apache-Spark-orange.svg)](https://spark.apache.org/)
[![Apache Mahout](https://img.shields.io/badge/Apache-Mahout-green.svg)](https://mahout.apache.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red.svg)](https://jupyter.org/)

> **Note: This repository is archived and no longer actively maintained.**

Comprehensive machine learning examples covering various frameworks and techniques including scikit-learn, Apache Spark, Apache Mahout, and Amazon Machine Learning services.

## 📁 Project Structure

- **[AI/](AI/)** - Java-based AI service examples (Polly, Rekognition)
- **[AmazonML/](AmazonML/)** - Amazon Machine Learning service examples
- **[Excel/](Excel/)** - Excel-based machine learning examples
- **[mahout/](mahout/)** - Apache Mahout examples
- **[scikit/](scikit/)** - scikit-learn examples and Jupyter notebooks
- **[Spark/](Spark/)** - Apache Spark machine learning examples

## 🚀 Getting Started

### Prerequisites

1. **Python**: Python 3.7 or higher
2. **Jupyter**: For notebook examples
3. **Java**: For Java-based examples
4. **Apache Spark**: For Spark examples
5. **Dependencies**: Install required packages

### Setup

1. **Install Python dependencies:**
   ```bash
   cd ML/scikit/
   pip install -r requirements.txt
   ```

2. **Install Jupyter:**
   ```bash
   pip install jupyter
   jupyter notebook
   ```

3. **Setup Java environment:**
   ```bash
   # For Java examples
   cd ML/AI/
   mvn install
   ```

## 🔧 Frameworks Covered

### scikit-learn
- Linear and Logistic Regression
- Decision Trees and Random Forest
- K-means Clustering
- Principal Component Analysis (PCA)
- XGBoost implementation

### Apache Spark
- Spark MLlib examples
- Large-scale machine learning
- Distributed computing
- Text classification (Spam detection)

### Apache Mahout
- Collaborative filtering
- Recommendation systems
- MovieLens dataset examples

### Amazon Machine Learning
- AWS ML service integration
- Banking dataset examples
- Batch and real-time predictions

### Java AI Services
- Amazon Polly integration
- Amazon Rekognition examples
- Face comparison and detection

## 📚 Examples Overview

### scikit-learn Examples
- **01 - Linear Regression.ipynb**: Basic linear regression
- **02 - Logistic Regression.ipynb**: Classification with logistic regression
- **02a - Logistic Regression on MNIST.ipynb**: MNIST digit classification
- **03 - Decision Trees.ipynb**: Decision tree implementation
- **03a - Random Forest.ipynb**: Ensemble methods
- **03b - XGBoost.ipynb**: Gradient boosting
- **04 - K-means.ipynb**: Clustering algorithms
- **05 - PCA.ipynb**: Dimensionality reduction
- **05a - PCA + Logistic Regression on MNIST.ipynb**: Combined techniques

### Spark Examples
- **spam.scala**: Spam classification using Spark MLlib
- **Spam classifier.json**: Model configuration
- **ham/ & spam/**: Training data directories

### Amazon ML Examples
- **MLSample.java**: Amazon ML service integration
- **banking.csv & banking-batch.csv**: Sample datasets
- **MLSample.IAM.txt**: IAM policy examples

### Java AI Examples
- **Polly.java**: Text-to-speech integration
- **RekoCompareFaces.java**: Face comparison
- **RekoDetectFaces.java**: Face detection
- **RekoDetectLabels.java**: Object detection

## 🛠️ Running Examples

### Jupyter Notebooks
```bash
cd ML/scikit/
jupyter notebook
```

### Python Scripts
```bash
cd ML/scikit/
python linearregression.py
python logisticregression.py
python decisiontrees.py
```

### Java Examples
```bash
cd ML/AI/
mvn compile exec:java -Dexec.mainClass="Polly"
```

### Spark Examples
```bash
cd ML/Spark/
spark-submit --class SpamClassifier spam.scala
```

## 📊 Datasets Used

- **MNIST**: Handwritten digit recognition
- **Banking**: Financial data for classification
- **MovieLens**: Movie ratings for recommendations
- **Spam/Ham**: Email classification data

## ⚠️ Important Notes

- **Dependencies**: Ensure all required packages are installed
- **Data**: Some examples require downloading datasets
- **AWS Credentials**: Required for AWS service examples
- **Memory**: Spark examples may require significant memory
- **SDK Versions**: Examples may use older library versions

## 🔗 Related Examples

- **[AmazonAI/](../AmazonAI/)** - AI service integration
- **[mxnet/](../mxnet/)** - Deep learning examples
- **[lambda_frameworks/](../lambda_frameworks/)** - ML Lambda functions

## 📖 Documentation

- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Apache Spark Documentation](https://spark.apache.org/docs/)
- [Apache Mahout Documentation](https://mahout.apache.org/)
- [Amazon ML Documentation](https://docs.aws.amazon.com/machine-learning/)

## 🎓 Learning Path

1. **Beginner**: Start with scikit-learn linear regression
2. **Intermediate**: Explore decision trees and clustering
3. **Advanced**: Work with Spark and distributed ML
4. **Expert**: Integrate with AWS ML services

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 