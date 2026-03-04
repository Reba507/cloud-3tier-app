# 3-Tier Containerized App on AWS

Simple Task Manager (Flask + PostgreSQL + Nginx)

Local test:
docker run -d -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=password postgres
docker build -t yourusername/cloud-3tier-app .
docker run -d -p 80:80 --name app \
  -e DB_HOST=host.docker.internal \
  -e DB_USER=postgres \
  -e DB_PASSWORD=password \
  -e DB_NAME=postgres \
  yourusername/cloud-3tier-app

Open http://localhost