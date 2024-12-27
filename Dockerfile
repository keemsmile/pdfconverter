# Use Python slim image
FROM python:3.11-slim

# Install system dependencies including Poppler
RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p output_images temp \
    && chmod -R 777 output_images temp

# Set environment variables
ENV POPPLER_PATH=/usr/bin \
    OUTPUT_DIR=/app/output_images \
    TEMP_DIR=/app/temp \
    PYTHONUNBUFFERED=1

# Expose Streamlit port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "webappconverter.py", "--server.address=0.0.0.0"]
