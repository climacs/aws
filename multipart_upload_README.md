# Multipart Upload Script

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS S3](https://img.shields.io/badge/AWS-S3-orange.svg)](https://aws.amazon.com/s3/)
[![Bash](https://img.shields.io/badge/Bash-Script-green.svg)](https://www.gnu.org/software/bash/)
[![Multipart](https://img.shields.io/badge/Multipart-Upload-blue.svg)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

> **Note: This repository is archived and no longer actively maintained.**

Bash script demonstrating multipart upload to Amazon S3 for large files, showing how to efficiently upload files larger than 5GB by splitting them into parts and uploading in parallel.

## 📁 Project Structure

- **[multipart.sh](multipart.sh)** - Multipart upload script for large files

## 🚀 Getting Started

### Prerequisites

1. **AWS CLI**: Install and configure AWS CLI
2. **Bash**: Bash shell environment
3. **AWS Account**: AWS account with S3 permissions
4. **Large File**: File to upload (typically > 5GB)

### Setup

1. **Install AWS CLI:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install awscli
   
   # macOS
   brew install awscli
   ```

2. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

3. **Make script executable:**
   ```bash
   chmod +x multipart.sh
   ```

## 🔧 Features Covered

### Multipart Upload
- **File splitting**: Split large files into manageable parts
- **Parallel upload**: Upload parts in parallel for better performance
- **Resume capability**: Resume interrupted uploads
- **Progress tracking**: Track upload progress

### S3 Integration
- **Bucket management**: Create and manage S3 buckets
- **Object upload**: Upload objects to S3
- **Metadata handling**: Handle file metadata
- **Error handling**: Robust error handling and recovery

### Performance Optimization
- **Chunk size optimization**: Optimize part sizes for performance
- **Concurrent uploads**: Upload multiple parts simultaneously
- **Bandwidth utilization**: Maximize bandwidth usage
- **Retry logic**: Automatic retry for failed parts

## 🛠️ Usage

### Basic Usage
```bash
./multipart.sh <local-file> <s3-bucket> <s3-key>
```

### Example
```bash
# Upload a large file to S3
./multipart.sh large-file.zip my-bucket uploads/large-file.zip
```

### Advanced Usage
```bash
# Upload with custom part size (in MB)
./multipart.sh large-file.zip my-bucket uploads/large-file.zip 100

# Upload with specific AWS profile
AWS_PROFILE=production ./multipart.sh large-file.zip my-bucket uploads/large-file.zip
```

## 🔌 Script Features

### File Splitting
```bash
# Split file into parts
split -b ${PART_SIZE}M "${LOCAL_FILE}" "${LOCAL_FILE}.part"
```

### Multipart Upload Initiation
```bash
# Initiate multipart upload
UPLOAD_ID=$(aws s3api create-multipart-upload \
    --bucket "${S3_BUCKET}" \
    --key "${S3_KEY}" \
    --query 'UploadId' \
    --output text)
```

### Part Upload
```bash
# Upload individual parts
aws s3api upload-part \
    --bucket "${S3_BUCKET}" \
    --key "${S3_KEY}" \
    --part-number "${PART_NUMBER}" \
    --upload-id "${UPLOAD_ID}" \
    --body "${PART_FILE}"
```

### Upload Completion
```bash
# Complete multipart upload
aws s3api complete-multipart-upload \
    --bucket "${S3_BUCKET}" \
    --key "${S3_KEY}" \
    --upload-id "${UPLOAD_ID}" \
    --multipart-upload "${PARTS_JSON}"
```

## ⚠️ Important Notes

- **File Size**: Multipart upload is recommended for files > 5GB
- **Part Limits**: Minimum 5MB, maximum 5GB per part
- **Concurrent Limits**: AWS has limits on concurrent multipart uploads
- **Costs**: Multipart uploads may have different pricing
- **Cleanup**: Failed uploads may leave incomplete parts

## 🔗 Related Examples

- **[serverlessPipeline/](../serverlessPipeline/)** - S3 data processing
- **[athena/](../athena/)** - S3 data querying
- **[bigdatabattle/](../bigdatabattle/)** - Large data processing

## 📖 Documentation

- [S3 Multipart Upload Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)
- [AWS CLI S3 Commands](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [S3 Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html)

## 🎯 Use Cases

### Large File Uploads
- **Backup files**: Large backup file uploads
- **Media files**: Video and audio file uploads
- **Data archives**: Large dataset uploads
- **Software distributions**: Large software package uploads

### Data Processing
- **ETL pipelines**: Large data file ingestion
- **Analytics**: Big data file uploads
- **Machine learning**: Large model file uploads
- **Content delivery**: Large content file uploads

### Backup and Recovery
- **System backups**: Large system backup uploads
- **Database dumps**: Large database backup uploads
- **Disaster recovery**: Large recovery file uploads
- **Archive storage**: Long-term archive uploads

## 💡 Best Practices

### Performance
- **Part size**: Use 100MB parts for optimal performance
- **Concurrency**: Upload 3-5 parts simultaneously
- **Retry logic**: Implement exponential backoff
- **Monitoring**: Monitor upload progress and performance

### Reliability
- **Error handling**: Handle network and AWS errors
- **Resume capability**: Support for resuming interrupted uploads
- **Validation**: Validate uploaded parts
- **Cleanup**: Clean up failed upload parts

### Security
- **Encryption**: Use server-side encryption
- **Access control**: Implement proper IAM policies
- **Audit logging**: Enable S3 access logging
- **Versioning**: Enable S3 versioning for important files

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 