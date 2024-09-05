#!/bin/sh
# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is up - executing migrations"
alembic upgrade head

pwd
# Start the application
exec uvicorn app.main:application --reload --host 0.0.0.0 --port 8000
