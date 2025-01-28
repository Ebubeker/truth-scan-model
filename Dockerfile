# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies if needed (e.g., for AI libraries like TensorFlow or PyTorch)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install Python dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the container
COPY . /app/

# Set the default command to run your AI script (adjust the script name as needed)
CMD ["python", "index.py"]  # Or replace `train.py` with your script name
