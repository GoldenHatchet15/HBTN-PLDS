# Docker Lecture – Beginner Friendly Deep Dive

## Holberton School – Cohort 25

---

# 🐳 I. Introduction to Docker

## What is Docker?

Docker is a platform that allows developers to package applications and everything they need into isolated environments called **containers**.

A container includes:

* Application code
* Libraries
* Dependencies
* Environment variables
* System tools
* Runtime

This means the application will behave the same way everywhere.

---

## The Problem Docker Solves

Before Docker, developers often faced this issue:

> “But it works on my machine…”

An application might work on:

* The developer’s laptop

But fail on:

* Another developer’s computer
* The production server
* The cloud deployment

Why?

Because every system may have:

* Different operating systems
* Different library versions
* Different dependencies
* Different configurations

Docker solves this by packaging everything together.

---

# 📦 What is a Container?

A container is an isolated environment that runs an application.

Think of it like:

* A mini-computer
* A lightweight virtual machine
* A portable box containing your app

---

## Real-Life Analogy

Imagine shipping containers on cargo ships.

Every container:

* Has everything packed inside
* Can be moved anywhere
* Works independently

Docker containers work similarly.

No matter where you run the container:

* Laptop
* Server
* Cloud

The application behaves consistently.

---

# 🖥️ Containers vs Virtual Machines

## Virtual Machine

A VM contains:

* Full operating system
* Virtual hardware
* Guest kernel

This makes them:

* Heavy
* Slow
* Resource expensive

---

## Docker Containers

Containers:

* Share the host OS kernel
* Are lightweight
* Start almost instantly
* Use fewer resources

---

# ⚡ Why Docker is Useful

## 1. Portability

Run the same app anywhere.

Example:

* Windows
* Linux
* Mac
* Cloud server

---

## 2. Isolation

Applications do not conflict with each other.

Example:

* One container uses Python 3.8
* Another uses Python 3.12

No issues.

---

## 3. Speed

Containers start in seconds.

Unlike VMs that may take minutes.

---

## 4. Scalability

You can launch multiple containers quickly.

Useful for:

* APIs
* Web servers
* Microservices

---

---

# 🐳 II. Core Docker Concepts

# 1. Docker Images

An image is:

* A template
* Read-only
* Used to create containers

Think of it like:

* A blueprint
* A recipe

---

## Example

Ubuntu image:

* Contains Ubuntu OS
* Basic tools
* Configuration

But it is NOT running yet.

---

# 2. Containers

A container is:

* A running instance of an image

Image = Blueprint
Container = Running house

---

# 3. Dockerfile

A Dockerfile is a text file containing instructions to build an image.

Example instructions:

* Install packages
* Copy files
* Run commands
* Start application

---

# 4. Docker Hub

Docker Hub is like GitHub for Docker images.

You can:

* Download images
* Share images
* Publish your own images

Examples:

* Ubuntu
* Python
* Nginx
* MongoDB

---

# 5. Docker Engine

Docker Engine is the software running on your computer that:

* Builds images
* Runs containers
* Manages networks
* Manages storage

---

---

# 🔧 III. Installing Docker

# Ubuntu Installation

```bash
sudo apt update
sudo apt install docker.io -y
```

---

# Verify Installation

```bash
docker --version
```

---

# Start Docker Service

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

# Test Docker

```bash
sudo docker run hello-world
```

This:

1. Downloads image
2. Creates container
3. Runs container
4. Prints success message

---

---

# 🧪 IV. Running Your First Container

# Launch Ubuntu Container

```bash
sudo docker run -it ubuntu
```

---

# Understanding the Command

## docker run

Creates and starts a container.

---

## -i

Interactive mode.

Keeps terminal open.

---

## -t

Creates terminal session.

---

## ubuntu

The image to use.

---

# Inside the Container

You may see:

```bash
root@container_id:/#
```

Now you are INSIDE the container.

---

# Test Commands

```bash
ls
pwd
uname -a
apt update
```

---

# Exit Container

```bash
exit
```

---

---

# 📋 V. Managing Containers

# Show Running Containers

```bash
docker ps
```

---

# Show All Containers

```bash
docker ps -a
```

---

# Stop Container

```bash
docker stop container_id
```

---

# Remove Container

```bash
docker rm container_id
```

---

# Remove Image

```bash
docker rmi image_name
```

---

---

# 🏗️ VI. Dockerfile Deep Dive

# What is a Dockerfile?

A Dockerfile is a set of instructions used to create a Docker image.

---

# Basic Dockerfile Structure

```Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

CMD ["python3"]
```

---

# Understanding Instructions

# FROM

Defines base image.

Example:

```Dockerfile
FROM ubuntu:latest
```

---

# RUN

Executes commands during build.

Example:

```Dockerfile
RUN apt-get update
```

---

# COPY

Copies files into image.

Example:

```Dockerfile
COPY . /app
```

---

# WORKDIR

Sets working directory.

Example:

```Dockerfile
WORKDIR /app
```

---

# CMD

Default command when container starts.

Example:

```Dockerfile
CMD ["python3", "app.py"]
```

---

---

# 🛠️ VII. Building Images

# Build Image

```bash
docker build -t myapp .
```

---

# Understanding the Command

## docker build

Builds image.

---

## -t

Adds image name (tag).

---

## .

Current directory.

Docker searches for:

* Dockerfile

---

# List Images

```bash
docker images
```

---

---

# 🌐 VIII. Flask API with Docker

# Flask API Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return {"message": "Hello World"}

app.run(host="0.0.0.0", port=5252)
```

---

# Why 0.0.0.0?

Important concept.

Inside Docker:

* localhost means INSIDE the container only

0.0.0.0 exposes the app externally.

Without it:

* Browser cannot access API

---

# Dockerfile for Flask

```Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install flask

CMD ["python", "app.py"]
```

---

# Build API

```bash
docker build -t flask-api .
```

---

# Run API

```bash
docker run -p 5252:5252 flask-api
```

---

# Understanding Port Mapping

```bash
-p 5252:5252
```

Structure:

```bash
HOST_PORT:CONTAINER_PORT
```

Meaning:

* Left = your computer
* Right = container

---

# Test API

Browser:

```text
http://localhost:5252/api/hello
```

---

---

# 🌍 IX. Nginx Front-End Container

# What is Nginx?

Nginx is:

* Web server
* Reverse proxy
* Load balancer

---

# Serve Static Website

```Dockerfile
FROM nginx:alpine

COPY ./static-site/ /usr/share/nginx/html
```

---

# What Happens?

Nginx automatically serves:

* HTML
* CSS
* JavaScript

---

# Run Container

```bash
docker run -p 8080:80 my-nginx
```

Visit:

```text
http://localhost:8080
```

---

---

# 🔗 X. Docker Networking

# Why Networking Matters

Containers are isolated.

But applications need communication.

Example:

* Frontend talks to API
* API talks to database

---

# Create Network

```bash
docker network create mynetwork
```

---

# Run Containers on Same Network

```bash
docker run --network mynetwork ...
```

---

# Container Communication

Containers can communicate by:

* Container name

Example:

```text
http://api:5252
```

---

---

# ⚖️ XI. Reverse Proxy & Load Balancing

# What is a Reverse Proxy?

A server that:

* Receives requests
* Forwards them to backend services

---

# Why Use Reverse Proxy?

## Security

Hide backend servers.

## Centralized Routing

One entry point.

## Load Balancing

Distribute traffic.

---

# Round Robin Load Balancing

Requests rotate between servers.

Example:

Request 1 → api1
Request 2 → api2
Request 3 → api1
Request 4 → api2

---

# Nginx Config Example

```nginx
http {

    upstream backend {
        server api1:5252;
        server api2:5252;
    }

    server {

        listen 80;

        location /api/ {
            proxy_pass http://backend;
        }

        location / {
            proxy_pass http://frontend;
        }
    }
}
```

---

# Important Concept

Nginx becomes:

* Traffic manager
* Gateway
* Router

---

---

# 🧩 XII. Docker Compose

# What is Docker Compose?

A tool to manage multiple containers together.

Instead of:

* Running many docker commands manually

You define everything in:

```text
docker-compose.yml
```

---

# Example

```yaml
version: '3'

services:

  api1:
    build: ./api

  api2:
    build: ./api

  frontend:
    build: ./frontend

  proxy:
    build: ./proxy
    ports:
      - "80:80"
```

---

# Docker Compose Commands

# Build Everything

```bash
docker compose build
```

---

# Start Everything

```bash
docker compose up
```

---

# Background Mode

```bash
docker compose up -d
```

---

# Stop Everything

```bash
docker compose down
```

---

---

# 🧹 XIII. Cleanup Commands

# Remove Unused Images

```bash
docker image prune
```

---

# Remove All Stopped Containers

```bash
docker container prune
```

---

# Remove Everything Unused

```bash
docker system prune
```

---

---

# 🧠 XIV. Common Beginner Mistakes

# 1. Forgetting Port Mapping

Without:

```bash
-p
```

Browser cannot access container.

---

# 2. Using localhost Incorrectly

Inside containers:

* localhost = same container only

---

# 3. Forgetting 0.0.0.0 in Flask

Without:

```python
host="0.0.0.0"
```

External access fails.

---

# 4. Confusing Images vs Containers

Image:

* Blueprint

Container:

* Running instance

---

---

# 🚀 XV. Real-World Uses of Docker

Docker is used for:

* APIs
* Databases
* Dev environments
* CI/CD pipelines
* Cloud deployment
* Microservices
* Web applications

Companies using Docker:

* Netflix
* Spotify
* Uber
* PayPal

---

---

# 🎯 XVI. Final Review

Students should now understand:

✅ What Docker is
✅ What containers are
✅ Images vs containers
✅ Dockerfiles
✅ Building images
✅ Running containers
✅ Flask APIs in Docker
✅ Nginx basics
✅ Networking
✅ Reverse proxies
✅ Load balancing
✅ Docker Compose

---

# 🏁 XVII. Practice Challenges

# Beginner

1. Run Ubuntu container
2. Install Python inside container
3. Exit container

---

# Intermediate

1. Create Flask API
2. Dockerize it
3. Expose port

---

# Advanced

1. Create frontend container
2. Create backend container
3. Connect with Docker Compose
4. Add reverse proxy

---

# 🐳 End of Lecture
