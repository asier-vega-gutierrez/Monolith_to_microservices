# Select the base image with the minimum space
FROM <select_image>

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define default env variables for the image
ENV <NAME> <VALUE>
...

ENV AM_I_IN_A_DOCKER_CONTAINER 1

# Copy requirements to code/requiremets.txt
# RUN pip install upgrade and pip install
<enter code here>

COPY ./src .

# Launch ENTRYPOINT command as array for 
ENTRYPOINT ["<comand>", "<par>", "<par>"]