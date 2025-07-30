FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy everything in your repo (including database.py, templates, etc.)
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run your Flask app
CMD ["python", "app.py"]
