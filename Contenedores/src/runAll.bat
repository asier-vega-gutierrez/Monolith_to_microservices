@echo off
title Run all containers

echo "Creating mucsi-docker-network"
docker network create mucsi-docker-network

echo "Creating zookeper"
docker run --rm -d --network mucsi-docker-network --network-alias zookeeper --name zookeeper -p 22181:2181 -e ZOOKEEPER_CLIENT_PORT=2181 -e ZOOKEEPER_TICK_TIME=200 -v './Kafka/kafka-storage/zookeeper/data:/var/lib/zookeeper/data' -v './Kafka/kafka-storage/zookeeper/log:/var/lib/zookeeper/log' confluentinc/cp-zookeeper:latest
echo "Creating Kafka"
timeout 5 > NUL
docker run --rm -d --network mucsi-docker-network --network-alias kafka --name kafka -p 29092:29092 -p 29093:29093 -e KAFKA_BROKER_ID=1 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 -e KAFKA_LISTENERS=EXTERNAL_SAME_HOST://:29092,EXTERNAL_DIFFERENT_HOST://:29093,INTERNAL://:9092 -e KAFKA_ADVERTISED_LISTENERS=INTERNAL://kafka:9092,EXTERNAL_SAME_HOST://localhost:29092,EXTERNAL_DIFFERENT_HOST://192.168.5.242:29093 -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=INTERNAL:PLAINTEXT,EXTERNAL_SAME_HOST:PLAINTEXT,EXTERNAL_DIFFERENT_HOST:PLAINTEXT -e KAFKA_INTER_BROKER_LISTENER_NAME=INTERNAL -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 -e KAFKA_CONFLUENT_LICENSE_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_CONFLUENT_BALANCER_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -v'./Kafka/kafka-storage/kafka/data:/var/lib/kafka/data' -v './Kafka/kafka-storage/kafka/secrets:/etc/kafka/secrets' confluentinc/cp-kafka:latest
echo "Creating Kafdrop"
timeout 5 > NUL
docker run --rm -d --network mucsi-docker-network --network-alias kafdrop --name kafdrop -p 9000:9000 -e KAFKA_BROKERCONNECT=kafka:9092 obsidiandynamics/kafdrop:latest 
echo "Creating MySQL DB"
docker run --rm -d --network mucsi-docker-network --network-alias mysql-input --name mysql-input -e MYSQL_ROOT_PASSWORD=MUCSI_Deusto2022 -e MYSQL_DATABASE=app_db -e MYSQL_USER=mucsi -e MYSQL_PASSWORD=MUCSI_Deusto2022 -p 3306:3306 -v './Storage/MySql_Input/data/db:/var/lib/mysql' mysql:latest
echo "Creating Sql Server DB"
docker run --rm -d --network mucsi-docker-network --network-alias sqlserver-input --name sqlserver-input -p 1433:1433 -e ACCEPT_EULA=Y -e SA_PASSWORD=MUCSI_Deusto2022 -e MSSQL_PID=Developer -v './Storage/azure-sql-edge/data:/var/opt/mssql/data' -v './Storage/azure-sql-edge/log:/var/opt/mssql/log' -v './Storage/azure-sql-edge/secrets:/var/opt/mssql/secrets' mcr.microsoft.com/azure-sql-edge
echo "Creating Postgres DB"
docker run --rm -d --network mucsi-docker-network --network-alias postgres-output --name postgres-output -p 5432:5432 -e POSTGRES_PASSWORD=MUCSI_Deusto2022 -e POSTGRES_DB=Foundry_Relational_Storage -v './Storage/Relational_Output/data:/var/lib/postgresql/data' postgres:15
echo "Creating Influx DB"
*** docker run --rm -d --network mucsi-docker-network --network-alias influxdb-output  --name influxdb-output -p <port>:<port> -e <env_var>=<value> -v '<local>:docker' <image>:<tag>

timeout 5 > NUL
echo "Creating PD Agent - MySQL"
docker run --rm -d --network mucsi-docker-network --network-alias pdagent-mysql-input --name pdagent-mysql-input -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_MYSQL_PROCESS_TOPIC=pouring_mysql -e MYSQL_IP=mysql-input -e MYSQL_PORT=3306 -e MYSQL_USER=root -e MYSQL_PASS=MUCSI_Deusto2022 -e MYSQL_DB=pouring pdagent_mysql:0.1
echo "Creating PD Agent - File CVS"
docker run --rm -d --network mucsi-docker-network --network-alias pdagent-file-input --name pdagent-file-input -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_CHEMICAL_COMPOSITION_TOPIC=chemical_composition_file -e COMPOSITION_FILE_PATH=/usr/src/app/cqfile/cq.csv -v './Storage/File_Input/data:/usr/src/app/cqfile' pdagent_file:0.1 
echo "Creating PD Agent - Sql Server"
docker run --rm -d --network mucsi-docker-network --network-alias pdagent-mssql-input --name pdagent-mssql-input -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_MOULD_DATA_TOPIC=mould_data -e KAFKA_SENSOR_DATA_TOPIC=sensor_data -e SQL_SERVER_IP=sqlserver-input -e SQL_SERVER_PORT=1433 -e SQL_SERVER_USER=sa -e SQL_SERVER_PASS=MUCSI_Deusto2022 -e SQL_SERVER_MOULD_DB=DB-MOULDING -e SQL_SERVER_SENSOR_DB=DB-SENSORS pdagent_sqlserver:0.1
echo "Creating Predictor for Cooling Drum"
*** docker run --rm -d --network mucsi-docker-network --network-alias cooling-drum-water-predictor --name cooling-drum-water-predictor -p <port>:<port> <image>:<tag>
echo "Creating Predictor for Belts"
docker run --rm -d --network mucsi-docker-network --network-alias belts-water-factor-predictor --name belts-water-factor-predictor -p 8090:80 belts_water_predictor:0.1
echo "Creating Digital Twin for L1"
docker run --rm -d --network mucsi-docker-network --network-alias l1-cooling-drum-digital-twin --name l1-cooling-drum-digital-twin -e DT_LINE=1 -e DT_MOULD_SIZE=20 -e DT_MOULDS_TO_CALCULATE=7 -e DT_TYPE=DRUM -e KAFKA_CLIENT_ID=WaterAddition-DigitalTwin-L1-cooling-drum -e KAFKA_GROUP_ID=Digital-Twin-Group-l1-cooling-drum -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_MOULD_FOR_BELTS_TOPIC=mould_for_belts -e KAFKA_PREDICTION_UNIFIED_BELTS_TOPIC=water_prediction_unified_belts -e KAFKA_PREDICTION_DRUM_TOPIC=water_prediction_cooling_drum -e KAFKA_MOULD_DATA_TOPIC=mould_data -e KAFKA_SENSOR_DATA_TOPIC=sensor_data -e COOLING_DRUM_API_BASE=http://cooling-drum-water-predictor:80/cooling-drum-water-prediction -e BELTS_API_BASE=http://belts-water-factor-predictor:80/unified_belt_prediction water_addition_digital_twin:0.1 
echo "Creating Digital Twin for L2"
docker run --rm -d --network mucsi-docker-network --network-alias l2-cooling-drum-digital-twin --name l2-cooling-drum-digital-twin -e DT_LINE=2 -e DT_MOULD_SIZE=30 -e DT_MOULDS_TO_CALCULATE=10 -e DT_TYPE=DRUM -e KAFKA_CLIENT_ID=WaterAddition-DigitalTwin-L2-cooling-drum -e KAFKA_GROUP_ID=Digital-Twin-Group-l2-cooling-drum -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_MOULD_FOR_BELTS_TOPIC=mould_for_belts -e KAFKA_PREDICTION_UNIFIED_BELTS_TOPIC=water_prediction_unified_belts -e KAFKA_PREDICTION_DRUM_TOPIC=water_prediction_cooling_drum -e KAFKA_MOULD_DATA_TOPIC=mould_data -e KAFKA_SENSOR_DATA_TOPIC=sensor_data -e COOLING_DRUM_API_BASE=http://cooling-drum-water-predictor:80/cooling-drum-water-prediction -e BELTS_API_BASE=http://belts-water-factor-predictor:80/unified_belt_prediction water_addition_digital_twin:0.1
echo "Creating Digital Twin for Belts"
docker run --rm -d --network mucsi-docker-network --network-alias tapes-digital-twin --name tapes-digital-twin -e DT_LINE=1 -e DT_MOULD_SIZE=30 -e DT_MOULDS_TO_CALCULATE=15 -e DT_TYPE=TAPES -e KAFKA_CLIENT_ID=WaterAddition-DigitalTwin-tapes -e KAFKA_GROUP_ID=Digital-Twin-Group-tapes -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_MOULD_FOR_BELTS_TOPIC=mould_for_belts -e KAFKA_PREDICTION_UNIFIED_BELTS_TOPIC=water_prediction_unified_belts -e KAFKA_PREDICTION_DRUM_TOPIC=water_prediction_cooling_drum -e KAFKA_MOULD_DATA_TOPIC=mould_data -e KAFKA_SENSOR_DATA_TOPIC=sensor_data -e COOLING_DRUM_API_BASE=http://cooling-drum-water-predictor:80/cooling-drum-water-prediction -e BELTS_API_BASE=http://belts-water-factor-predictor:80/unified_belt_prediction water_addition_digital_twin:0.1
echo "Creating PD Agent - Correlation Output"
docker run --rm -d --network mucsi-docker-network --network-alias pdagent-relational-output --name pdagent-relational-output -e KAFKA_CLIENT_ID=DB-Relational-Storage-Agent -e KAFKA_GROUP_ID=DB-Relational-DB-Writer -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_POR=9092 -e KAFKA_SENSOR_DATA_TOPIC=sensor_data_ -e KAFKA_CHEMICAL_COMPOSITION_TOPIC=chemical_composition_file -e KAFKA_WATER_PREDICTION_DRUM_TOPIC=water_prediction_cooling_drum_ -e KAFKA_WATER_PREDICTION_TAPES_TOPIC=water_prediction_unified_belts -e KAFKA_POURING_DATA_TOPIC=pouring_mysql -e KAFKA_MOULD_DATA_TOPIC=mould_data_ -e POSTGRES_IP=postgres-output -e POSTGRES_PORT=5432 -e POSTGRES_USER=postgres -e POTSGRES_PASS=MUCSI_Deusto2022 -e POSTGRES_DB=Foundry_Relational_Storage pdagent_relational_storage:0.1 
echo "Creating PD Agent - Temporal Series"
docker run --rm -d --network mucsi-docker-network --network-alias pdagent-temporal-serie-output --name pdagent-temporal-serie-output -e KAFKA_CLIENT_ID=Influx-DB-Storage-Agent -e KAFKA_GROUP_ID=TemporalSeries-Writer-Group -e KAFKA_BROKER_IP=kafka -e KAFKA_BROKER_PORT=9092 -e KAFKA_DRUM_WATER_PREDICTION_TOPIC=water_prediction_cooling_drum -e KAFKA_BELTS_WATER_PREDICTION_TOPIC=water_prediction_unified_belts -e KAFKA_SENSOR_DATA_TOPIC=sensor_data -e INFLUX_TOKEN=_vunCmVedzTMarNJ4y4iwTGpFU84gerPj7sDyAlwJuHpMKFyjc187bhpGsYZwDVaTnJz4nZ2esU-MZ3UlNVFRA== -e INFLUX_URL=http://influxdb-output:8086 -e INFLUX_ORG=Deusto -e INFLUX_BUCKET=cloud-bucket pdagent_temporal_serie:0.1
echo "Creating Grafana"
docker run --rm -d --network mucsi-docker-network --network-alias grafana --name grafana -p 3000:3000 -v './Storage/grafana/data:/var/lib/grafana' -e GF_SECURITY_ADMIN_USER=mucsi -e GF_SECURITY_ADMIN_PASSWORD=MUCSI_Deusto2022 -e GF_INSTALL_PLUGINS= grafana/grafana-enterprise

pause