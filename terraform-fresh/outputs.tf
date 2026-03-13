output "instance_ip" {
  value = aws_instance.app.public_ip
}

output "instance_url" {
  value = "http://${aws_instance.app.public_dns}"
}

output "alb_dns" {
  value = aws_lb.app.dns_name
}

output "application_url" {
  value = "http://${aws_lb.app.dns_name}"
}

output "rds_endpoint" {
  value     = aws_db_instance.main.endpoint
  sensitive = true
}
