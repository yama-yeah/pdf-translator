FROM python:slim

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt