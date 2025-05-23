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
docker build -t pdagent_sqlserver:0.1 ./PDAgents/PDAgent_SqlServerReader
docker build -t digital_twin_l1:0.1 ./Digital_Twin/l1-cooling-drum-digital-twin
docker build -t digital_twin_l2:0.1 ./Digital_Twin/l2-cooling-drum-digital-twin
docker build -t digital_twin_tapes:0.1 ./Digital_Twin/tapes-digital-twin
docker build -t pdagent_relational_storage:0.1 ./PDAgents/PDAgent_RelationDBWriter
docker build -t pdagent_temporal_serie:0.1 ./PDAgents/PDAgent_TemporalSeriesWriter

REM Build API Rest Images with names: cooling_drum_water_predictor:0.1 and belts_water_predictor:0.1
docker build -t cooling_drum_water_predictor:0.1 ./Predictions/CoolingDrumWaterAddition
docker build -t belts_water_predictor:0.1 ./Predictions/BeltsWaterAdditionFactor
