# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the service code
COPY . .

# Expose the port
EXPOSE 5001

# Run the app
CMD ["python", "app.py"]