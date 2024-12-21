# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set environment variables in Dockerfile
ENV HOST=0.0.0.0
ENV PORT=8000	

# Set the working directory in the container
WORKDIR /app/

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./app /app/app

# Expose the port the app runs on
EXPOSE $PORT

# Command to run the application using environment variables
CMD uvicorn app.main:app --host $HOST --port $PORT		