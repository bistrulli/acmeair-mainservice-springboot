#!/bin/bash

IMAGE_NAME="rpizziol/acmeair-mainservice-springboot"
TAG="0.10"

docker build --no-cache -t $IMAGE_NAME:$TAG . && docker push $IMAGE_NAME:$TAG
