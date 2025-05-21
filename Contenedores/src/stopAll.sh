#!/bin/sh

# We stop all containers
docker stop grafana
docker stop pdagent-temporal-serie-output
docker stop pdagent-relational-output
docker stop tapes-digital-twin
docker stop l2-cooling-drum-digital-twin
docker stop l1-cooling-drum-digital-twin
docker stop belts-water-factor-predictor
docker stop cooling-drum-water-predictor
docker stop pdagent-mssql-input
docker stop pdagent-file-input
docker stop pdagent-mysql-input
docker stop influxdb-output 
docker stop postgres-output
docker stop sqlserver-input
docker stop mysql-input
docker stop kafdrop
docker stop kafka
docker stop zookeeper

# We delete the network
docker network rm mucsi-docker-network