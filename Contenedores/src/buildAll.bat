@echo off
title Build all images

REM Download external images
REM docker pull confluentinc/cp-zookeeper:latest
REM docker pull confluentinc/cp-kafka:latest
REM docker pull obsidiandynamics/kafdrop:latest  
REM docker pull mysql:8.1
REM docker pull mcr.microsoft.com/azure-sql-edge
REM docker pull postgres:15
REM docker pull influxdb:latest
REM docker pull grafana/grafana-enterprise

REM Build our own images
docker build -t pdagent_mysql:0.1 ./PDAgents/PDAgent_MySqlReader
docker build -t pdagent_file:0.1 ./PDAgents/PDAgent_FileReader
REM docker build -t pdagent_sqlserver:0.1 ./PDAgents/PDAgent_SqlServerReader
REM docker build -t water_addition_digital_twin:0.1 ./Digital_Twin
REM docker build -t pdagent_relational_storage:0.1 ./PDAgents/PDAgent_RelationDBWriter
REM docker build -t pdagent_temporal_serie:0.1 ./PDAgents/PDAgent_TemporalSeriesWriter

REM Build API Rest Images with names: cooling_drum_water_predictor:0.1 and belts_water_predictor:0.1
REM docker build ...
REM docker build ...
