# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.11-slim

# Install only nginx (no extra packages)
RUN apt-get update && apt-get install -y nginx curl && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /etc/nginx/sites-enabled/default

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

# Copy application code
COPY app.py .
COPY requirements.txt .
COPY start.sh .
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY templates/ ./templates/

# Make start script executable
RUN chmod +x start.sh

# Create nginx log directory
RUN mkdir -p /var/log/nginx

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:80/health || exit 1

EXPOSE 80

CMD ["./start.sh"]