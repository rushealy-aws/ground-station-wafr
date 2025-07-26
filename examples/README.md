# Examples

This directory contains practical examples and automation tools to support AWS Ground Station Well Architected reviews and implementations.

## 📁 Contents

### CloudFormation Templates

#### `cloudformation-monitoring.yaml`
A comprehensive CloudFormation template for setting up Ground Station monitoring and alerting infrastructure.

**Features:**
- CloudWatch dashboard for Ground Station metrics
- SNS topic and email notifications for alerts
- Custom Lambda function for additional metrics collection
- IAM roles with least privilege permissions
- EventBridge rules for automated metric collection

**Usage:**
```bash
aws cloudformation create-stack \
  --stack-name ground-station-monitoring \
  --template-body file://cloudformation-monitoring.yaml \
  --parameters ParameterKey=NotificationEmail,ParameterValue=your-email@example.com \
               ParameterKey=GroundStationRegion,ParameterValue=us-east-1 \
  --capabilities CAPABILITY_NAMED_IAM
```

**Parameters:**
- `NotificationEmail`: Email address for receiving alerts
- `GroundStationRegion`: AWS region where Ground Station antennas are located

### Python Scripts

#### `contact-scheduler.py`
An automated contact scheduling script that demonstrates best practices for Ground Station operations.

**Features:**
- Automated conflict detection and resolution
- Optimal contact window calculation
- Integration with CloudWatch metrics
- Command-line interface for easy automation
- Error handling and logging

**Prerequisites:**
```bash
pip install boto3 python-dateutil
```

**Usage:**
```bash
# Schedule a contact with automatic optimization
python contact-scheduler.py \
  --satellite-id NOAA-18 \
  --start-time 2025-01-27T10:00:00Z \
  --duration 600 \
  --mission-profile-arn arn:aws:groundstation:us-east-1:123456789012:mission-profile/12345678-1234-1234-1234-123456789012

# Dry run to see optimal window without scheduling
python contact-scheduler.py \
  --satellite-id NOAA-18 \
  --start-time 2025-01-27T10:00:00Z \
  --duration 600 \
  --mission-profile-arn arn:aws:groundstation:us-east-1:123456789012:mission-profile/12345678-1234-1234-1234-123456789012 \
  --dry-run
```

**Command Line Options:**
- `--satellite-id`: Satellite identifier (required)
- `--start-time`: Preferred start time in ISO format (required)
- `--duration`: Contact duration in seconds (required)
- `--mission-profile-arn`: Mission profile ARN (required)
- `--region`: AWS region (default: us-east-1)
- `--dry-run`: Calculate optimal window without scheduling

## 🚀 Getting Started

### Prerequisites

1. **AWS CLI configured** with appropriate permissions
2. **Python 3.7+** for Python examples
3. **Ground Station permissions** for your AWS account
4. **Well Architected Tool access** for lens import

### Required AWS Permissions

The examples require the following AWS permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "groundstation:*",
        "cloudwatch:PutMetricData",
        "cloudwatch:GetMetricStatistics",
        "sns:Publish",
        "lambda:InvokeFunction",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}
```

### Setup Instructions

1. **Clone or download** the examples to your local environment
2. **Configure AWS credentials** using `aws configure` or environment variables
3. **Install dependencies** for Python examples:
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   # Or install individually:
   pip install boto3 python-dateutil
   ```
4. **Customize parameters** in the examples for your specific use case
5. **Test in a development environment** before using in production

## 📋 Best Practices Demonstrated

### Operational Excellence
- **Automated scheduling** with conflict resolution
- **Comprehensive logging** and error handling
- **Infrastructure as Code** using CloudFormation
- **Monitoring and alerting** setup

### Security
- **Least privilege IAM roles** and policies
- **Secure parameter handling** in CloudFormation
- **No hardcoded credentials** in code examples
- **Proper error handling** without exposing sensitive information

### Reliability
- **Error handling and retry logic** in automation scripts
- **Monitoring and alerting** for system health
- **Backup and recovery considerations** in templates
- **Graceful degradation** in failure scenarios

### Performance Efficiency
- **Optimal resource allocation** in CloudFormation
- **Efficient API usage** in Python scripts
- **Appropriate timeout and retry settings**
- **Resource cleanup** and lifecycle management

### Cost Optimization
- **Right-sized resources** in templates
- **Automated resource management** to prevent waste
- **Cost-effective monitoring** strategies
- **Usage tracking and optimization** features

## 🔧 Customization Guide

### Adapting for Your Environment

1. **Update Region Settings**: Modify region parameters for your Ground Station locations
2. **Customize Monitoring**: Adjust CloudWatch metrics and alarms for your requirements
3. **Modify Scheduling Logic**: Adapt the contact scheduler for your satellite constellation
4. **Add Organization Policies**: Include your organization's specific requirements

### Adding New Examples

When contributing new examples:

1. **Follow naming conventions**: Use descriptive, kebab-case filenames
2. **Include documentation**: Add clear README sections and inline comments
3. **Test thoroughly**: Ensure examples work in multiple environments
4. **Follow security best practices**: No hardcoded credentials or sensitive data
5. **Include error handling**: Robust error handling and logging

## 🐛 Troubleshooting

### Common Issues

#### CloudFormation Deployment Fails
- **Check permissions**: Ensure your AWS credentials have CloudFormation and service permissions
- **Validate template**: Use `aws cloudformation validate-template` before deployment
- **Review parameters**: Ensure all required parameters are provided and valid

#### Python Script Errors
- **Check dependencies**: Ensure all required Python packages are installed
- **Verify credentials**: Confirm AWS credentials are configured correctly
- **Review permissions**: Ensure your AWS user/role has Ground Station permissions
- **Check regions**: Verify the specified region has Ground Station antennas

#### Ground Station API Errors
- **Service availability**: Confirm Ground Station is available in your region
- **Resource limits**: Check if you've reached any service limits
- **Satellite parameters**: Verify satellite IDs and orbital parameters are correct
- **Mission profiles**: Ensure mission profiles are properly configured

### Getting Help

1. **Check AWS documentation**: [Ground Station User Guide](https://docs.aws.amazon.com/ground-station/latest/ug/)
2. **Review CloudWatch logs**: Check Lambda and CloudWatch logs for detailed error messages
3. **Use AWS Support**: Contact AWS Support for service-specific issues
4. **Community resources**: Check AWS forums and community discussions

## 📚 Additional Resources

### AWS Documentation
- [AWS Ground Station User Guide](https://docs.aws.amazon.com/ground-station/latest/ug/)
- [Ground Station API Reference](https://docs.aws.amazon.com/ground-station/latest/APIReference/)
- [CloudFormation Ground Station Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html)

### Best Practices
- [Ground Station Best Practices](https://docs.aws.amazon.com/ground-station/latest/ug/best-practices.html)
- [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/)
- [CloudWatch Best Practices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html)

### Training and Certification
- [AWS Ground Station Technical Essentials](https://aws.amazon.com/training/)
- [AWS Solutions Architect Certification](https://aws.amazon.com/certification/certified-solutions-architect-associate/)

---

## 🤝 Contributing

We welcome contributions to improve these examples! Please see our [Contributing Guidelines](../CONTRIBUTING.md) for details on how to submit improvements, report issues, or add new examples.

## 📄 License

These examples are provided under the MIT License. See the [LICENSE](../LICENSE) file for details.
