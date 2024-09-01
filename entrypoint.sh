#!/bin/sh
# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is up - executing migrations"
alembic revision --autogenerate -m "First commit"
alembic upgrade head

# Start the application
exec uvicorn app.main:application --reload --host 0.0.0.0 --port 8000
