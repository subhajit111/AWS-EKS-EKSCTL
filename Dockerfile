# Use an official Python runtime as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Define the command to run your Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
