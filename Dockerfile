FROM docker.io/ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
	cmake make gunicorn nginx python3 python3-pip python3-setuptools build-essential \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN mkdir -p /home/app
RUN chmod -R 777 /home/app

WORKDIR /

COPY app /home/app
RUN chmod -R 777 /home/app

WORKDIR /home/app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "--timeout", "90", "--bind", ":5000", "api:app"]