# FLASK DEVOPS APP

A simple flask web app containerized with Docker.

## Run locally
python app.py

## Option - 1: Run with Docker
docker build -t flaskapp .  
docker run -p 5000:5000 flaskapp

## Option - 2: Pull from Docker Hub(recommended)
docker pull mdaashir10/flaskapp01:latest  
docker run -p 5000:5000 mdaashir10/flaskapp01:latest

Live: https://python-flaskapp-bvvf.onrender.com
