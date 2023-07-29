# Use a base image with Python installed
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Expose the port that the server will be running on
EXPOSE 8000

# Set the environment variable to tell Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Set the entry point command to run the server
CMD ["python", "server/app.py"]
