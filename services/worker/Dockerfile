#FROM pytorch/pytorch:latest-gpu
#FROM python:3.10-slim
FROM nvidia/cuda:12.4.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y python3 python3-pip git


ENV PYTHONUNBUFFERED=1
WORKDIR /app

#RUN apt-get update && apt-get install -y    libgl1    libglib2.0-0    git \
#    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir tqdm opencv-python-headless nudenet>=3.4.2 nc_py_api

COPY worker.py .

CMD ["python3", "worker.py"]
