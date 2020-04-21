FROM alpine:3.8
RUN apk add --update python3 py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY static /src/static
COPY templates /src/templates
CMD python /src/app.py
