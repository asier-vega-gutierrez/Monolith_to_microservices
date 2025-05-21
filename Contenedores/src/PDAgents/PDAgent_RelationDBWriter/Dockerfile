FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define default env variables for the image
ENV <NAME> <VALUE>
...

ENV AM_I_IN_A_DOCKER_CONTAINER 1

COPY ./requirements.txt .
RUN pip install --upgrade pip

# We install some packages because the image does not have them installed
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps



# Copy requirements to code/requiremets.txt
# RUN pip install upgrade and pip install
<enter code here>

COPY ./src .

# Launch ENTRYPOINT command as array for 
ENTRYPOINT ["<comand>", "<par>", "<par>"]