#!/bin/sh

# This images are build on Contenedores folder go there to build them then execute this to upload them to the registry
# The parameter $1 is the registry key, which is passed when running the script.


docker tag pdagent_mysql:0.1 cloudregistryasier.azurecr.io/pdagent_mysql:0.1
docker tag pdagent_file:0.1 cloudregistryasier.azurecr.io/pdagent_file:0.1
docker tag pdagent_sqlserver:0.1 cloudregistryasier.azurecr.io/pdagent_sqlserver:0.1
docker tag digital_twin_l1:0.1 cloudregistryasier.azurecr.io/digital_twin_l1:0.1
docker tag digital_twin_l2:0.1 cloudregistryasier.azurecr.io/digital_twin_l2:0.1
docker tag digital_twin_tapes:0.1 cloudregistryasier.azurecr.io/digital_twin_tapes:0.1
docker tag pdagent_relational_storage:0.1 cloudregistryasier.azurecr.io/pdagent_relational_storage:0.1
docker tag pdagent_temporal_serie:0.1 cloudregistryasier.azurecr.io/pdagent_temporal_serie:0.1
docker tag belts_water_predictor:0.1 cloudregistryasier.azurecr.io/belts_water_predictor:0.1
docker tag cooling_drum_water_predictor:0.1 cloudregistryasier.azurecr.io/cooling_drum_water_predictor:0.1



docker login cloudregistryasier.azurecr.io -u cloudregistryasier -p $1


docker push cloudregistryasier.azurecr.io/pdagent_mysql:0.1
docker push cloudregistryasier.azurecr.io/pdagent_file:0.1
docker push cloudregistryasier.azurecr.io/pdagent_sqlserver:0.1
docker push cloudregistryasier.azurecr.io/digital_twin_l1:0.1
docker push cloudregistryasier.azurecr.io/digital_twin_l2:0.1
docker push cloudregistryasier.azurecr.io/digital_twin_tapes:0.1
docker push cloudregistryasier.azurecr.io/pdagent_relational_storage:0.1
docker push cloudregistryasier.azurecr.io/pdagent_temporal_serie:0.1
docker push cloudregistryasier.azurecr.io/belts_water_predictor:0.1
docker push cloudregistryasier.azurecr.io/cooling_drum_water_predictor:0.1