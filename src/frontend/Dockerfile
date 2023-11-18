FROM ubuntu:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip python3-dev

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080 

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "skkuppt.wsgi:application"]
#CMD ["python3", "manage.py", "runserver","0.0.0.0:8080"]


