#!/bin/sh

# This files execute the services need to have the images uploaded to the registry

kubectl apply -f .
kubectl apply -f DB/.
kubectl apply -f DigitalTwin/.
kubectl apply -f Kafka/.
kubectl apply -f PDagents/.
kubectl apply -f Predictions/.