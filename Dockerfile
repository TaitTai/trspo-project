FROM python:3.10-slim

RUN apt-get update && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

EXPOSE 12345

CMD ["python", "server.py"]
