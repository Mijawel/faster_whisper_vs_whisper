FROM python:3.9
RUN apt-get update -y
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential python-dev
RUN apt-get install -y ffmpeg

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "python3", "./main.py"]