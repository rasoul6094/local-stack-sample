FROM python:3.8



WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl unzip \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt install zip -y
RUN apt install less -y

COPY . .



RUN  chmod +x /app/localstack/deploy.sh


RUN python manage.py makemigrations
RUN python manage.py migrate

CMD  ["sh", "-c", "cd /app && /app/localstack/deploy.sh "]