# Select the base image with the minimum space
FROM python:3.13-alpine

# Define the work dir
WORKDIR /usr/src/app

# Define ENV variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy and launch the code
COPY ./src .
ENTRYPOINT ["python", "main.py", "--start"]
