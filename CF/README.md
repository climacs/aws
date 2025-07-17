# AWS CloudFormation & Infrastructure as Code

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS CloudFormation](https://img.shields.io/badge/AWS-CloudFormation-orange.svg)](https://aws.amazon.com/cloudformation/)
[![Terraform](https://img.shields.io/badge/Terraform-HashiCorp-purple.svg)](https://www.terraform.io/)
[![Troposphere](https://img.shields.io/badge/Troposphere-Python-blue.svg)](https://github.com/cloudtools/troposphere)

> **Note: This repository is archived and no longer actively maintained.**

Infrastructure as Code examples using AWS CloudFormation, Terraform, and Troposphere for automated AWS resource provisioning and management.

## 📁 Project Structure

- **[cfdemo/](cfdemo/)** - CloudFormation template examples
- **[terraform/](terraform/)** - Terraform infrastructure examples
- **[troposphere/](troposphere/)** - Python-based infrastructure generation

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Terraform**: For Terraform examples (optional)
4. **Python**: For Troposphere examples (optional)

### Setup

1. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

2. **Install Terraform (for Terraform examples):**
   ```bash
   # Download from https://www.terraform.io/downloads.html
   # or use package manager
   brew install terraform  # macOS
   ```

3. **Install Troposphere (for Python examples):**
   ```bash
   pip install troposphere
   ```

## 🔧 Examples Covered

### CloudFormation Templates
The `cfdemo/` folder contains various CloudFormation templates:
- **Basic infrastructure**: VPC, subnets, security groups
- **Application stacks**: LAMP stack, web applications
- **Template versions**: Progressive improvements and fixes
- **Best practices**: Proper resource organization and naming

### Terraform Examples
The `terraform/` folder contains Terraform configurations:
- **Basic infrastructure**: Simple resource creation
- **Modular design**: Reusable infrastructure components
- **State management**: Proper Terraform state handling

### Troposphere Examples
The `troposphere/` folder contains Python-based infrastructure:
- **Programmatic templates**: Generate CloudFormation from Python
- **Dynamic resources**: Conditional resource creation
- **Template validation**: Built-in validation capabilities

## 📚 Examples Overview

### CloudFormation Examples
- **template0.json**: Basic template structure
- **template1.json**: LAMP stack template
- **template1v2.json - template1v5.json**: Progressive improvements
- **vpc1.json**: VPC and networking template
- **lamp.json**: Complete LAMP stack
- **demo.txt**: Template usage instructions

### Terraform Examples
- **ex1/ex1.tf**: Basic resource creation
- **ex2/ex2.tf**: Intermediate infrastructure
- **ex3/ex3.tf**: Advanced configurations

### Troposphere Examples
- **ex1.py**: Basic Troposphere usage
- **demo.txt**: Troposphere examples and instructions

## 🛠️ Running Examples

### CloudFormation Deployment
```bash
cd CF/cfdemo/
aws cloudformation create-stack \
    --stack-name my-stack \
    --template-body file://template1.json \
    --capabilities CAPABILITY_IAM
```

### Terraform Deployment
```bash
cd CF/terraform/ex1/
terraform init
terraform plan
terraform apply
```

### Troposphere Template Generation
```bash
cd CF/troposphere/
python ex1.py > generated_template.json
```

## 🏗️ Infrastructure Patterns

### Basic VPC Setup
```yaml
# CloudFormation example
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
```

### Security Group Configuration
```yaml
# Security group with common rules
  WebSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Web server security group
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
```

## ⚠️ Important Notes

- **Cost**: CloudFormation creates real AWS resources that incur costs
- **Permissions**: Ensure proper IAM permissions for resource creation
- **Dependencies**: Some templates depend on other resources
- **Regions**: Templates may be region-specific
- **Limits**: Be aware of AWS service limits

## 🔗 Related Examples

- **[lambda_frameworks/](../lambda_frameworks/)** - Serverless infrastructure
- **[ecs/](../ecs/)** - Container infrastructure
- **[serverlessPipeline/](../serverlessPipeline/)** - Complex architectures

## 📖 Documentation

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [CloudFormation Template Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html)
- [Terraform AWS Provider](https://www.terraform.io/docs/providers/aws/)
- [Troposphere Documentation](https://github.com/cloudtools/troposphere)

## 💡 Best Practices

### CloudFormation
- **Use parameters**: Make templates reusable
- **Add descriptions**: Document your resources
- **Use conditions**: Conditional resource creation
- **Validate templates**: Use `aws cloudformation validate-template`
- **Use nested stacks**: Break down complex templates

### Terraform
- **Use modules**: Reusable infrastructure components
- **Manage state**: Use remote state storage
- **Use variables**: Make configurations flexible
- **Plan before apply**: Always review changes
- **Use workspaces**: Environment separation

### General
- **Version control**: Track infrastructure changes
- **Documentation**: Document your infrastructure
- **Testing**: Test templates in non-production
- **Monitoring**: Monitor resource costs and usage
- **Backup**: Backup state files and templates

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 