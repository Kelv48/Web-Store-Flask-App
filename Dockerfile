# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
