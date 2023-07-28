# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the required files and directories into the container
COPY . /app

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y gcc

# Install Python dependencies
RUN pip install  -r requirements.txt

# Expose the port used by your application (if any)
# EXPOSE <port_number>

CMD ["python", "server/app.py"]
