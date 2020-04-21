FROM alpine:latest
MAINTAINER Srujan Deshpande srujan.deshpande@gmail.com
RUN apt-get install -y python3-pip python3-dev build-essential
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY static /src/static
COPY templates /src/templates
CMD python /src/app.py
