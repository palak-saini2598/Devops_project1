# CI/CD Pipeline with Docker & Jenkins
This project demonstrates a basic Continuous Integration / Continuous Deployment (CI/CD) pipeline that automates the build, test, and deployment of an application using Docker and Jenkins.

# Overview
The goal of this project is to show how code changes can automatically move from development to production with minimal manual work.
The pipeline builds a Docker image of the application, pushes it to DockerHub, and can be deployed anywhere that supports Docker.

# Step-by-Step Workflow
## Create a Dockerfile
Define a base image.
Copy application files into the container.
Install dependencies.
Specify the command to run the app.

Benefit: Ensures the app runs the same way on every machine.

## Build the Docker Image
docker build -t plk25/plkimage:v1 .
Creates a portable image containing the app and all dependencies.

## Push the Image to DockerHub
docker login
docker push plk25/plkimage:v1
Makes the image publicly available so it can be pulled and run anywhere.

## Set Up Jenkins CI/CD
Install and configure Jenkins.
Create a new job/pipeline that:
Pulls the latest code from GitHub.
Builds the Docker image using the Dockerfile.
Pushes the image to DockerHub automatically.

## Key Learnings
Docker: Building and packaging apps into reproducible containers.
Jenkins: Automating build, test, and deployment steps.

DevOps Workflow: Integrating Git, Docker, DockerHub, and Jenkins for a seamless development-to-deployment pipeline.

## Tech Stack
Docker
Jenkins
Git & GitHub
DockerHub
