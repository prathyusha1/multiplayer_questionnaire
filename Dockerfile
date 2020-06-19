FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && \
apt-get install -y nodejs && \
pip install -r requirements.txt 
COPY . /code/
RUN chmod +x script.sh
