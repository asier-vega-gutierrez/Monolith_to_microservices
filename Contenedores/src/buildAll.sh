#!/bin/sh

# Download images for services
# Image needed: confluentinc/cp-zookeeper:latest
# Image needed: confluentinc/cp-kafka:latest
# Image needed: obsidiandynamics/kafdrop:latest  
# Image needed: mysql:latest
# Image needed: mcr.microsoft.com/azure-sql-edge
# Image needed: postgres:15
# Image needed: influxdb:latest
# Image needed: grafana/grafana-enterprise
docker pull <image>:<tag>

# Build our own images
docker build -t pdagent_mysql:0.1 ./PDAgents/PDAgent_MySqlReader
docker build -t pdagent_file:0.1 ./PDAgents/PDAgent_FileReader
docker build -t pdagent_sqlserver:0.1 ./PDAgents/PDAgent_SqlServerReader
docker build -t cooling_drum_water_predictor:0.1 ./Predictions/CoolingDrumWaterAddition
docker build -t pdagent_relational_storage:0.1 ./PDAgents/PDAgent_RelationDBWriter
docker build -t pdagent_temporal_serie:0.1 ./PDAgents/PDAgent_TemporalSeriesWriter

# Build API Rest Images with names: cooling_drum_water_predictor:0.1 and belts_water_predictor:0.1
docker build ...
docker build ...