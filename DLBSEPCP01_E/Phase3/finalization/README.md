# AWS Static Website Deployment using Terraform

## Description
This project deploys a static website on AWS using:
- S3 (storage & hosting)
- CloudFront (CDN & HTTPS)
- IAM (secure access)

## Requirements
- AWS Account
- Terraform installed " be sure that The directory has Terraform configuration files "
- AWS CLI configured

## How to Run

1. Initialize Terraform
   terraform init

2. Preview the deployment
   terraform plan

3. Apply configuration
   terraform apply

4. Access the website
   Use the CloudFront URL from outputs

## Notes
- Infrastructure is fully automated using Terraform
- No manual AWS setup required