# Start from the official Python base image
FROM python:3.7-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt before other files
# Utilise Docker cache to save re-installing dependencies if unchanged
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files
COPY . .

# Expose the listening port
EXPOSE 5001

# Run the Flask app
CMD ["python", "./src/app.py"]