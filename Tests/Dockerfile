# Use the official Python base image
FROM python:3.11-slim

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# Run the test application
CMD ["pytest"]