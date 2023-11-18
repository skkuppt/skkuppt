FROM rockylinux/rockylinux:9.2

RUN dnf -y update && \
    dnf -y install gcc make python3 python3-pip python3-devel && \
    dnf clean all

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "skkuppt.wsgi:application"]


