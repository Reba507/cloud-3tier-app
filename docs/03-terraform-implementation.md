# Terraform Implementation

## Infrastructure as Code Structure
terraform/
├── main.tf # Main configuration file
├── variables.tf # Input variables
├── outputs.tf # Output values
└── terraform.tfvars # Variable values (not in repo)

text

## Key Resources Created

### Networking
```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
}

resource "aws_subnet" "public_1" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
}