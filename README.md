# 3-Tier Containerized Application on AWS

## Project Overview
A scalable 3-tier web application deployed on AWS using Terraform, Docker, and CI/CD.

## Architecture
- **Presentation Tier**: Nginx reverse proxy + Flask web app
- **Application Tier**: Flask (Python) CRUD application
- **Data Tier**: PostgreSQL (RDS)

## AWS Infrastructure
- Custom VPC with public/private subnets
- Application Load Balancer
- EC2 instances (Dockerized)
- RDS PostgreSQL
- NAT Gateway for outbound traffic
- Security Groups with least privilege
- IAM roles for EC2
- SSM Parameter Store for secrets

## Technologies Used
- **IaC**: Terraform
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Monitoring**: CloudWatch
- **Web Server**: Nginx
- **App Framework**: Flask
- **Database**: PostgreSQL

## Project Structure
├── .github/workflows/ # CI/CD pipelines
├── terraform/ # Infrastructure as Code
├── docs/ # Documentation & diagrams
├── app.py # Flask application
├── Dockerfile # Container definition
├── nginx/ # Nginx configuration
├── requirements.txt # Python dependencies
├── start.sh # Container startup script
└── templates/ # HTML templates

text

## Deployment Steps
1. **Clone repository**
2. **Configure AWS credentials**
3. **Run Terraform**: `cd terraform && terraform apply`
4. **Build and push Docker image**: `docker build -t yourusername/app . && docker push`
5. **Access application**: `http://<alb-dns-name>`

## Screenshots
[Add screenshots here]

## Challenges & Solutions
- **vCPU Limits**: Reached AWS account limits, documented as learning experience
- **Security Group Configuration**: Implemented proper chaining
- **Database Connection**: Used SSM Parameter Store for credentials

## Future Improvements
- Implement Auto Scaling when vCPU limits increase
- Add Prometheus/Grafana monitoring
- Implement Blue/Green deployment
