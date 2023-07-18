# WebApp for ReAnimate: A Learning platform - Yankun (Alex) Meng

My goal is to develop a full-stack web application for ReAnimate while also extending it to beyond an augmented reality App. My vision is to make it a brand new learning platform where, students, researchers, and publishers can publish papers and resources on the site, and everyone could learn in a collaborative environment. Features such as augmented reality will be added, as well as additional features such as internationalization.

## Running Backend

### Docker Setup

Run a Container:

docker run -d -p 80:80 docker/getting-started

docker ps -- check status

### Postgres Database setup

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

1. Create IAM User in AWS
2. Add Security credentials, store access keys in local machine

## Citations

[Install Docker](https://www.docker.com/) <br>
[Postgres Database](https://www.postgresql.org/) <br>
[AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/) <br>
Amigoscode: [Tutorial](https://youtu.be/9i1gQ7w2V24)


