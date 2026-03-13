# Architecture Design

## Network Architecture





## VPC Configuration
| Resource | Configuration |
|----------|--------------|
| VPC CIDR | 10.0.0.0/16 |
| Public Subnet 1 | 10.0.1.0/24 (us-east-1a) |
| Public Subnet 2 | 10.0.2.0/24 (us-east-1b) |
| Private Subnet 1 | 10.0.3.0/24 (us-east-1a) |
| Private Subnet 2 | 10.0.4.0/24 (us-east-1b) |

## Routing
- **Public Subnets**: Route to Internet Gateway (0.0.0.0/0)
- **Private Subnets**: Route to NAT Gateway for outbound internet

## High Availability Design
- Resources distributed across two Availability Zones
- Application Load Balancer distributes traffic
- RDS Multi-AZ (configured but not enabled due to cost)
- Auto Scaling configured (disabled due to vCPU limits)

## Scalability Strategy
- **Vertical Scaling**: Instance size increase (t2.micro → t2.medium)
- **Horizontal Scaling**: Auto Scaling group (1-3 instances)
- **Scaling Triggers**: CPU utilization >70% scale up, <30% scale down