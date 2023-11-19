FROM ubuntu:latest

RUN apt-get update \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip python3-dev

WORKDIR /

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

