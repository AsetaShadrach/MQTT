FROM python:3.8-alpine
WORKDIR /.
RUN apk add build-base
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
COPY --chmod=755 entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]