# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY server.py .

# Expose port 8080 for the MCP server
EXPOSE 5000

# Default command (can be overridden)
CMD ["python", "server.py"]