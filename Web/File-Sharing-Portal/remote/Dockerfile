# Use a base image with Python
FROM python:3.9-slim

# Copy the Flask application code
COPY srv/ /app/

RUN apt-get update && \
    apt-get install -y cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    cd /app/ && pip install --no-cache-dir -r requirements.txt && \
    mkdir /etc/cron.custom && \
    echo "*/5 * * * * root rm -rf /app/uploads/*" > /etc/cron.custom/cleanup-cron && \
    echo "* * * * * root cd / && run-parts --report /etc/cron.custom" | tee -a /etc/crontab && \
    chmod 555 /etc/cron.custom/cleanup-cron && \
    crontab /etc/cron.custom/cleanup-cron && \
    crontab /etc/crontab && \
    mkdir /var/log/cron

# Set up the working directory
WORKDIR /app

# Start cron and Flask server
ENTRYPOINT ["sh", "-c", "cron && python server.py"]
