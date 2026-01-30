FROM python:3.9-slim

WORKDIR /app
COPY app.py /app

RUN apt-get update && apt-get install -y python3-tk

CMD ["python3", "app.py"]

