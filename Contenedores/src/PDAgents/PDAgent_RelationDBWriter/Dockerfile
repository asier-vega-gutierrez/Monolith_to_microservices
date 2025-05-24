FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define default env variables for the image
ENV KAFKA_CLIENT_ID=DB-Relational-Storage-Agent 
ENV KAFKA_GROUP_ID=DB-Relational-DB-Writer 
ENV KAFKA_BROKER_IP=kafka  
ENV KAFKA_BROKER_POR=9092 
ENV KAFKA_SENSOR_DATA_TOPIC=sensor_data 
ENV KAFKA_CHEMICAL_COMPOSITION_TOPIC=chemical_composition_file 
ENV KAFKA_WATER_PREDICTION_DRUM_TOPIC=water_prediction_cooling_drum
ENV KAFKA_WATER_PREDICTION_TAPES_TOPIC=water_prediction_unified_belts 
ENV KAFKA_POURING_DATA_TOPIC=pouring_mysql 
ENV KAFKA_MOULD_DATA_TOPIC=mould_data
ENV POSTGRES_IP=postgres-output 
ENV POSTGRES_PORT=5432 
ENV POSTGRES_USER=postgres 
ENV POTSGRES_PASS=MUCSI_Deusto2022 
ENV POSTGRES_DB=Foundry_Relational_Storage 

ENV AM_I_IN_A_DOCKER_CONTAINER=1

# We install some packages because the image does not have them installed
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# Copy and launch the code
COPY ./src .
ENTRYPOINT ["python", "main.py"]