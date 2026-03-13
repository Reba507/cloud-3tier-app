#!/bin/bash
# start.sh - Optimized version

# Function to handle shutdown
cleanup() {
    echo "Shutting down services..."
    kill -TERM "$GUNICORN_PID" 2>/dev/null
    kill -TERM "$NGINX_PID" 2>/dev/null
    exit 0
}

trap cleanup SIGTERM SIGINT

# Start Gunicorn with optimized settings
echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:5000 \
    --workers 2 \
    --threads 2 \
    --worker-class gthread \
    --access-logfile - \
    --error-logfile - \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    app:app &
GUNICORN_PID=$!

# Wait for Gunicorn to start
sleep 3

# Start Nginx
echo "Starting Nginx..."
nginx -g 'daemon off;' &
NGINX_PID=$!

# Wait for both processes
wait $GUNICORN_PID $NGINX_PID