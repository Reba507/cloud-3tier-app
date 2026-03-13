variable "region" {
  description = "AWS Region"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for tagging"
  default     = "cloud-3tier"
}

variable "docker_image" {
  description = "Docker image for the application"
  default     = "rebaone20/cloud-3tier-app:latest"
}

# Existing resource IDs (optional - leave empty to create new)
variable "existing_vpc_id" {
  description = "Use existing VPC instead of creating new one"
  type        = string
  default     = ""
}

variable "existing_public_subnet_1" {
  description = "Use existing public subnet 1"
  type        = string
  default     = ""
}

variable "existing_public_subnet_2" {
  description = "Use existing public subnet 2"
  type        = string
  default     = ""
}

variable "existing_private_subnet_1" {
  description = "Use existing private subnet 1"
  type        = string
  default     = ""
}

variable "existing_private_subnet_2" {
  description = "Use existing private subnet 2"
  type        = string
  default     = ""
}

variable "existing_igw_id" {
  description = "Use existing Internet Gateway"
  type        = string
  default     = ""
}