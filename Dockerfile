FROM python:3.12-slim

# Install system dependencies needed for building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Add verbose output to see actual error
RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .
# Collect static files and start gunicorn
CMD ["sh", "-c", "python api/manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 --chdir api config.wsgi:application"]