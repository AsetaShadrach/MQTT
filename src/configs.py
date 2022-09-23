import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import paho.mqtt.client as mqtt
from flask_migrate import Migrate


app = Flask(__name__)


MQTT_BROKER_URL = os.environ.get('MQTT_BROKER_URL')  # use the free broker from HIVEMQ
MQTT_BROKER_PORT = int(os.environ.get('MQTT_BROKER_PORT')) # default port for non-tls connection
MQTT_USERNAME = os.environ.get('MQTT_USERNAME')  # set the username here if you need authentication for the broker
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD')  # set the password here if the broker demands authentication
MQTT_KEEPALIVE = int(os.environ.get('MQTT_KEEPALIVE'))  # set the time interval for sending a ping to the broker to 5 seconds
MQTT_TLS_ENABLED = False if os.environ.get('MQTT_TLS_ENABLED') == "False" else True # set TLS to disabled for testing purposes
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

basedir = os.path.abspath(os.path.dirname(__file__))


client = mqtt.Client("prod")
