# Amazon ECS Examples

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/yourusername/aws)
[![AWS ECS](https://img.shields.io/badge/AWS-ECS-orange.svg)](https://aws.amazon.com/ecs/)
[![Docker](https://img.shields.io/badge/Docker-Containers-blue.svg)](https://www.docker.com/)
[![Fargate](https://img.shields.io/badge/AWS-Fargate-green.svg)](https://aws.amazon.com/fargate/)

> **Note: This repository is archived and no longer actively maintained.**

Amazon ECS (Elastic Container Service) examples demonstrating container orchestration, task definitions, and service management for scalable containerized applications.

## 📁 Project Structure

- **[ecs-find](ecs-find)** - ECS service discovery and management
- **[updateAgent.sh](updateAgent.sh)** - ECS agent update script

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **Docker**: Docker installed for container management
4. **ECS CLI**: ECS command-line interface (optional)

### Setup

1. **Install ECS CLI:**
   ```bash
   # Download ECS CLI
   curl -Lo ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest
   chmod +x ecs-cli
   sudo mv ecs-cli /usr/local/bin/
   ```

2. **Configure ECS CLI:**
   ```bash
   ecs-cli configure profile --profile-name default --access-key YOUR_ACCESS_KEY --secret-key YOUR_SECRET_KEY
   ecs-cli configure --cluster my-cluster --region us-east-1 --default-launch-type FARGATE
   ```

3. **Create ECS cluster:**
   ```bash
   aws ecs create-cluster --cluster-name my-cluster
   ```

## 🔧 Examples Covered

### Container Management
- **Task definitions**: Container specifications and configurations
- **Service management**: Service deployment and scaling
- **Cluster management**: ECS cluster operations
- **Agent updates**: ECS agent maintenance

### Deployment Strategies
- **Blue-green deployment**: Zero-downtime deployments
- **Rolling updates**: Gradual service updates
- **Service discovery**: Container-to-container communication
- **Load balancing**: Application load balancing

### Monitoring and Maintenance
- **Service discovery**: Finding and connecting to services
- **Health checks**: Container health monitoring
- **Logging**: Container log management
- **Scaling**: Automatic and manual scaling

## 📚 Examples Overview

### Management Scripts
- **ecs-find**: Service discovery and management utility
- **updateAgent.sh**: ECS agent update automation

## 🛠️ Running Examples

### Create Task Definition
```bash
# Create task definition JSON
cat > task-definition.json << EOF
{
    "family": "my-app",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "256",
    "memory": "512",
    "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
    "containerDefinitions": [
        {
            "name": "my-app",
            "image": "nginx:latest",
            "portMappings": [
                {
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ]
        }
    ]
}
EOF

# Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json
```

### Create Service
```bash
# Create ECS service
aws ecs create-service \
    --cluster my-cluster \
    --service-name my-service \
    --task-definition my-app:1 \
    --desired-count 2 \
    --launch-type FARGATE \
    --network-configuration "awsvpcConfiguration={subnets=[subnet-12345],securityGroups=[sg-12345],assignPublicIp=ENABLED}"
```

### Update ECS Agent
```bash
# Run agent update script
chmod +x updateAgent.sh
./updateAgent.sh
```

## 🔌 ECS Components

### Task Definition
```json
{
    "family": "web-app",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "256",
    "memory": "512",
    "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
    "containerDefinitions": [
        {
            "name": "web",
            "image": "nginx:latest",
            "portMappings": [
                {
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/web-app",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]
}
```

### Service Definition
```bash
# Service with load balancer
aws ecs create-service \
    --cluster my-cluster \
    --service-name web-service \
    --task-definition web-app:1 \
    --desired-count 3 \
    --launch-type FARGATE \
    --network-configuration "awsvpcConfiguration={subnets=[subnet-1,subnet-2],securityGroups=[sg-12345],assignPublicIp=ENABLED}" \
    --load-balancers "targetGroupArn=arn:aws:elasticloadbalancing:region:account:targetgroup/web-tg,containerName=web,containerPort=80"
```

## ⚠️ Important Notes

- **Costs**: ECS services incur costs based on resource usage
- **Networking**: Configure VPC, subnets, and security groups properly
- **Scaling**: Monitor service performance and adjust capacity
- **Security**: Use IAM roles and security groups for access control
- **Monitoring**: Set up CloudWatch alarms for service health

## 🔗 Related Examples

- **[CF/](../CF/)** - Infrastructure as Code for ECS
- **[lambda_frameworks/](../lambda_frameworks/)** - Serverless alternatives
- **[iot/](../iot/)** - Containerized IoT applications

## 📖 Documentation

- [Amazon ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [ECS Task Definition Reference](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)
- [ECS Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
- [ECS CLI Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI.html)

## 🎯 Use Cases

### Web Applications
- **Microservices**: Containerized microservice architecture
- **Web servers**: Nginx, Apache, and custom web applications
- **API services**: RESTful API backends

### Data Processing
- **Batch processing**: Containerized batch jobs
- **ETL pipelines**: Data transformation workflows
- **Analytics**: Real-time analytics applications

### DevOps
- **CI/CD pipelines**: Continuous integration and deployment
- **Monitoring**: Containerized monitoring solutions
- **Testing**: Automated testing environments

## 💡 Best Practices

### Container Design
- **Multi-stage builds**: Optimize container images
- **Security scanning**: Scan images for vulnerabilities
- **Resource limits**: Set appropriate CPU and memory limits
- **Health checks**: Implement container health checks

### Service Management
- **Auto scaling**: Configure automatic scaling policies
- **Service discovery**: Use service discovery for communication
- **Load balancing**: Implement proper load balancing
- **Monitoring**: Set up comprehensive monitoring

### Security
- **IAM roles**: Use least-privilege IAM roles
- **Security groups**: Restrict network access
- **Secrets management**: Use AWS Secrets Manager
- **Image scanning**: Regularly scan container images

---

**Last updated**: 2024  
**Status**: Archived - No longer actively maintained 