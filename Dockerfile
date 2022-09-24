FROM python:3.7-alpine
WORKDIR /.
RUN apk add build-base
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]