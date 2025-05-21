# Select the base image with the minimum space
FROM python:3.13-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define default env variables for the image
ENV KAFKA_BROKER_IP=kafka 
ENV KAFKA_BROKER_POR=9092
ENV KAFKA_MYSQL_PROCESS_TOPIC=pouring_mysql
ENV MYSQL_ROOT_PASSWORD=MUCSI_Deusto2022 
ENV MYSQL_DATABASE=app_db 
ENV MYSQL_USER=root 
ENV MYSQL_PASSWORD=MUCSI_Deusto2022 
ENV AM_I_IN_A_DOCKER_CONTAINER=1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy and launch the code
COPY ./src .
ENTRYPOINT ["python", "main.py"]