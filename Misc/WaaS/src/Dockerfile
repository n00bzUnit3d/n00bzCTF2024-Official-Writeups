# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY chall.py /app/
COPY try.py /app/
COPY fake_flag.txt /app/
COPY flag.txt /app/


CMD ["python", "try.py"]
