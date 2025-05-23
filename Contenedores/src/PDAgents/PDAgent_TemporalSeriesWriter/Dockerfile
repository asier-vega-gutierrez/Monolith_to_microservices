# Select the base image with the minimum space
FROM python:3.13-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define default env variables for the image
ENV KAFKA_CLIENT_ID=Influx-DB-Storage-Agent 
ENV KAFKA_GROUP_ID=TemporalSeries-Writer-Group 
ENV KAFKA_BROKER_IP=kafka 
ENV KAFKA_BROKER_PORT=9092 
ENV KAFKA_DRUM_WATER_PREDICTION_TOPIC=water_prediction_cooling_drum 
ENV KAFKA_BELTS_WATER_PREDICTION_TOPIC=water_prediction_unified_belts 
ENV KAFKA_SENSOR_DATA_TOPIC=sensor_data 
ENV INFLUX_TOKEN=vunCmVedzTMarNJ4y4iwTGpFU84gerPj7sDyAlwJuHpMKFyjc187bhpGsYZwDVaTnJz4nZ2esU-MZ3UlNVFRA== 
ENV INFLUX_URL=http://influxdb-output:8086 
ENV INFLUX_ORG=Deusto 
ENV INFLUX_BUCKET=cloud-bucket 
ENV AM_I_IN_A_DOCKER_CONTAINER=1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy and launch the code
COPY ./src .
ENTRYPOINT ["python", "main.py"]