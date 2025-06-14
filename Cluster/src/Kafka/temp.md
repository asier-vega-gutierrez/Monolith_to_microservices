__consumer_offsets
chemical_composition_file
mould_data_l1
mould_data_l2
mould_for_belts
pouring_mysql
sensor_data_l1
sensor_data_l2
water_prediction_cooling_drum_l1
water_prediction_cooling_drum_l2
water_prediction_unified_belts

kafka-topics --bootstrap-server localhost:9092 --list

kafka-topics --bootstrap-server localhost:9092 --describe --topic chemical_composition_file
kafka-topics --bootstrap-server localhost:9092 --create \
  --topic chemical_composition_file \
  --partitions 1 \
  --replication-factor 1


kafka-topics --bootstrap-server localhost:9092 --describe --topic mould_data_l1
kafka-topics --bootstrap-server localhost:9092 --create \
  --topic mould_data_l1 \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic mould_data_l2 \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic mould_for_belts \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic pouring_mysql \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic sensor_data_l1 \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic sensor_data_l2 \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic water_prediction_cooling_drum_l1 \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic water_prediction_cooling_drum_l2 \
  --partitions 1 \
  --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --create \
  --topic water_prediction_unified_belts \
  --partitions 1 \
  --replication-factor 1


kafka-topics --bootstrap-server localhost:9092 --create \
  --topic chemical_composition_file \
  --partitions 1 \
  --replication-factor 1


kafka-topics --bootstrap-server localhost:9092 --describe --topic mould_data_l1

kafka-topics --bootstrap-server localhost:9092 --create --topic mould_data_l1 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic mould_data_l2 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic mould_for_belts --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic pouring_mysql --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic sensor_data_l1 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic sensor_data_l2 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic water_prediction_cooling_drum_l1 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic water_prediction_cooling_drum_l2 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic water_prediction_unified_belts --partitions 1 --replication-factor 1
  