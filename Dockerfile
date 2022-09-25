FROM python:3.8-slim-buster
WORKDIR /MQTT
COPY . .
RUN pip install -r requirements.txt
# make shell scripts executable
RUN chmod u+x scripts/*.sh

ENTRYPOINT ["/MQTT/scripts/start_server.sh"]
