# Project Overview: 3-Tier Cloud Application on AWS

## Project Goal
Design and deploy a scalable, containerized 3-tier web application on AWS using Infrastructure as Code (Terraform) and CI/CD automation.

## Business Scenario
A startup requires a highly available web application hosted on AWS. The solution must be scalable, secure, cost-optimized, and follow AWS Well-Architected Framework principles.

## Technologies Used
| Component | Technology |
|-----------|------------|
| **Frontend** | HTML, Jinja2 templates |
| **Backend** | Flask (Python) |
| **Web Server** | Nginx (reverse proxy) |
| **Database** | PostgreSQL (Amazon RDS) |
| **Containerization** | Docker |
| **Infrastructure as Code** | Terraform |
| **CI/CD** | GitHub Actions |
| **Cloud Provider** | AWS (us-east-1) |
| **Monitoring** | CloudWatch |

## Architecture Overview
- **Presentation Tier**: Nginx serves static files and proxies requests to the Flask application
- **Application Tier**: Flask application handles business logic and CRUD operations
- **Data Tier**: PostgreSQL database stores task data
- **Networking**: Custom VPC with public/private subnets, NAT Gateway, Internet Gateway
- **Load Balancing**: Application Load Balancer distributes traffic
- **Security**: IAM roles, Security Groups, Parameter Store for secrets

## Key Features
- Task management CRUD functionality
- Containerized application for portability
- Infrastructure defined as code
- Automated CI/CD pipeline
- Database encryption at rest
- Secure secret management
- Load-balanced traffic distribution