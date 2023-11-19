FROM ubuntu:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y pkg-config libmysqlclient-dev \
    && apt-get install -y python3 python3-pip python3-dev

WORKDIR /

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080 

ENV GUNICORN_WORKERS=3

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

