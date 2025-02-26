# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "--app", "main.py", "--debug", "run", "--host=0.0.0.0", "--port=5000"]