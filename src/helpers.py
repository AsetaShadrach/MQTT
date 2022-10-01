import logging
import json
import random, string
from src.models import Recording, Device
from src.configs import client, db
from datetime import datetime

# MQTT INITIATE/CHECK CONNECTION
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Add other topics here
        client.subscribe("TEMPERATURE")
        client.subscribe("PH")
        client.subscribe("DTH")
        logging.info(f"=== Connection SUCCESSFULL at {datetime,datetime.now()} ===")
    else:    
        logging.info(f"=== Connection FAILED at {datetime,datetime.now()} ===")

# MQTT PROCESS MESSAGES
def on_message(client, userdata, msg):
    if msg.payload.decode().startswith('{'):
        topic = msg.topic 
        msg = msg.payload.decode()
        data = json.loads(msg)
        # TODO : Check for token in message
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
            logging.error(e)
        
    else:
        pass

# MQTT LOGGING
def on_log(client, userdata, level, buf):
    # print("log: ",level, buf.values)

    # TODO : Find a way to logg accordingly, 
    # or use python default logging better
    pass

# CREATE DEVICE TOKEN
def create_token():
    generated_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

    # If the token already exists try create another
    while device:=Device.query.filter_by(token=generated_token).first():
        generated_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        
    return generated_token

# REGISTER NEW DEVICE ON DB
def add_device(name, topic, device_details=None):
    token = create_token()
    logging.info(f" TOKEN GENERATED IS : {token}")
    # TODO :send response to device with the token

    try:
        device  = Device(
            name = name,
            topic= topic.upper(),
            device_details = device_details,
            token = token
        )
        db.session.add(device)
        db.session.commit()
        print("SUCCESSFULLY CREATED DEVICE")
        logging.info(f"Device with details {device} created")
        return {
            "status": 200,
            "message": "Device creation successful",
            "response": device.serialize()
        }

    except Exception as e:
        logging.error(e.with_traceback())
        return {
            "status": 400,
            "message": "Device creation failed",
            "response": str(e)
        }

# GET ALL DEVICES 
def get_devices():
    # TODO : Add filters for get request
    try:
        result = Device.query.all()
        return {
            "status": 200,
            "message": "Succesful",
            "response": Device.serialize_list(result)
        }
    except Exception as e:
        logging.error(e.with_traceback())
        return {
            "status": 400,
            "message": "Failed",
            "response": str(e)
        }
    

def get_device_by_id(id):
    # TODO : Add filters for get request
    try:
        device = Device.query.filter_by(id=id).first()
        if device:
            response = {
                "status": 200,
                "message": "Successfully retreived device data",
                "response": device.serialize()
            }
        else:
            response =  {
                "status": 404,
                "message": "Device not found",
                "response": f"No device with ID {id}"
            }
        
        return response

    except Exception as e:
        logging.error(e.with_traceback())
        return {
                "status": 500,
                "message": str(e),
                "response": str(e)
            }

def get_recordings():
    # TODO : Add filters for get request
    try:
        result = Recording.query.all()
        return {
                "status": 200,
                "message": "Succesful",
                "response": Recording.serialize_list(result)
            }
    except Exception as e:
        logging.error(e.with_traceback())
        return {
            "status": 400,
            "message": "Failed",
            "response": str(e)
        }
    

def get_recording_by_id(id):
    # TODO : Add filters for get request
    try:
        record = Recording.query.filter_by(id=id).first()
        if record:
            response = {
                "status": 200,
                "message": "Successfully retreived recording data",
                "response": record.serialize()
            }
        else:
            response =  {
                "status": 404,
                "message": "Record not found",
                "response": f"No record with ID {id}"
            }
        
        return response

    except Exception as e:
        logging.error(e.with_traceback())
        return {
                "status": 500,
                "message": str(e),
                "response": str(e)
            }


