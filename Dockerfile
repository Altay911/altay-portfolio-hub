FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# We run from the 'api' folder where manage.py lives
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "api", "config.wsgi:application"]