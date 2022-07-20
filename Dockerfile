# syntax=docker/dockerfile:1
FROM python:3.10.5-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY file_metadata.py file_metadata.py
CMD [ "python3", "file_metadata.py"]