import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import paho.mqtt.client as mqtt
from flask_migrate import Migrate
import sys

app = Flask(__name__)

MQTT_BROKER_URL = os.environ.get('MQTT_BROKER_URL')  # use the free broker from HIVEMQ
MQTT_BROKER_PORT = int(os.environ.get('MQTT_BROKER_PORT')) # default port for non-tls connection
MQTT_USERNAME = os.environ.get('MQTT_USERNAME')  # set the username here if you need authentication for the broker
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD')  # set the password here if the broker demands authentication
MQTT_KEEPALIVE = int(os.environ.get('MQTT_KEEPALIVE'))  # set the time interval for sending a ping to the broker to 5 seconds
MQTT_TLS_ENABLED = False if os.environ.get('MQTT_TLS_ENABLED') == "False" else True # set TLS to disabled for testing purposes
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

basedir = os.path.abspath(os.path.dirname(__file__))

client = mqtt.Client("prod")

# Initialize our ngrok settings into Flask
app.config.from_mapping(
    BASE_URL="http://localhost:5000",
    USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
)

if os.environ.get("ENV") == "development" and os.environ.get("USE_NGROK")=="True":
    # pyngrok will only be installed, and should only ever be initialized, in a dev environment
    from pyngrok import ngrok

    # Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
    # when starting the server
    port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000

    # Open a ngrok tunnel to the dev server
    public_url = ngrok.connect(port).public_url
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

    # Update any base URLs or webhooks to use the public ngrok URL
    app.config["BASE_URL"] = public_url
    # init_webhooks(public_url)
