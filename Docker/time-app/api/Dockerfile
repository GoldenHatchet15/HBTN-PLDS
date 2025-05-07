FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask pytz

# Make sure the app runs as the main module
CMD ["python", "-u", "app.py"]