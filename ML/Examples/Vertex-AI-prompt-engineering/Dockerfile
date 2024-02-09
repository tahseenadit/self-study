# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Setup application home and python path.
ENV APP_HOME /app/
ENV PYTHONPATH="$PYTHONPATH:$APP_HOME"

WORKDIR $APP_HOME

COPY requirements.txt .

# We mount the secret `service_account_key` to auth towards the python repo in IDEA-Core-Prod
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY app ./app
COPY public ./public

WORKDIR $APP_HOME/app

# Define environment variable
ENV NAME World

# Run the web service on container startup. Here we use the gunicorn webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn -k uvicorn.workers.UvicornWorker --bind :8080 --workers 1 --threads 8 --timeout 0 app.main:app
