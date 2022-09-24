import logging
import json
from src.models import Recording, Device
from src.configs import client, db, MQTT_BROKER_URL
from datetime import datetime 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Add other topics here
        client.subscribe("TEMPERATURE")
        client.subscribe("PH")
        client.subscribe("DTH")
        print("connection successful")
    else:    
        print("FAILED TO ESTABLISH CONNECTION")


def on_message(client, userdata, msg):
    if msg.payload.decode().startswith('{'):
        topic = msg.topic 
        msg = msg.payload.decode()
        data = json.loads(msg)
        try:        
            logging.info(" === Initiate saving record === ")
            recording = Recording(
                topic = topic,
                value = float(data["value"]),
                device_id = data["device_id"]
            )
            db.session.add(recording)
            db.session.commit()

            print("SUCCESSFULLY SAVED RECORD")
            logging.info(f"Record with details {recording} saved")

        except Exception as e:
            logging.error(e.with_traceback())
        
    else:
        pass