# Select the base image with the minimum space
FROM python:3.13-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define default env variables for the image
ENV DT_LINE=1 
ENV DT_MOULD_SIZE=20 
ENV DT_MOULDS_TO_CALCULATE=7 
ENV DT_TYPE=DRUM 
ENV KAFKA_CLIENT_ID=WaterAddition-DigitalTwin-L1-cooling-drum 
ENV KAFKA_GROUP_ID=Digital-Twin-Group-l1-cooling-drum 
ENV KAFKA_BROKER_IP=kafka 
ENV KAFKA_BROKER_PORT=9092 
ENV KAFKA_MOULD_FOR_BELTS_TOPIC=mould_for_belts 
ENV KAFKA_PREDICTION_UNIFIED_BELTS_TOPIC=water_prediction_unified_belts 
ENV KAFKA_PREDICTION_DRUM_TOPIC=water_prediction_cooling_drum 
ENV KAFKA_MOULD_DATA_TOPIC=mould_data 
ENV KAFKA_SENSOR_DATA_TOPIC=sensor_data 
ENV COOLING_DRUM_API_BASE=http://cooling-drum-water-predictor:80/cooling-drum-water-prediction 
ENV BELTS_API_BASE=http://belts-water-factor-predictor:80/unified_belt_prediction 

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy and launch the code
COPY ./src .
ENTRYPOINT ["python", "main.py"]