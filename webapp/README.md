# Web Application for ReAnimate: A Learning platform

## Running Backend

### Docker Setup

[Install Docker](https://www.docker.com/) <br>

Run a Container:

docker run -d -p 80:80 docker/getting-started

docker ps -- check status

### Database setup

[Postgres Database](https://www.postgresql.org/)

docker-compose.yml

docker compose up -d

docker logs postgres 

docker exec -it postgres sh

## Running Frontend

### Node.js 18.16.1 LTS

cd frontend/react

npm install to get node_modules

npm run dev

## AWS

[AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/)

1. Create IAM User in AWS
2. Add Security credentials, store access keys in local machine


