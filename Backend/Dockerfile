# Use the official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install Flask

# Expose the port that Flask runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=5000
ENV FLASK_ENV=development

# Run the Flask application
CMD ["flask", "run"]