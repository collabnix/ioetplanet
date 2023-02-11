# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the script to the image
COPY tello.py .

# Install the necessary dependencies
RUN pip install python-tello

# Set the command to run when the container starts
CMD ["python", "tello.py"]
