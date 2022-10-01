from flask import request,jsonify 
from src import app
from src.helpers import (
   add_device, get_devices, get_device_by_id,
    get_recordings, get_recording_by_id, client
   )

# Check if this thing is up
@app.route('/')
@app.route('/home')
def hello():
    return "Hi there! Service is up.", 200

@app.route('/publish', methods=['POST'])
def publish_message():
   request_data = request.get_json()
   publish_result = client.publish(request_data['topic'], request_data['message'])
   if publish_result.rc == 0:
      return jsonify({"code":200}), 200
   return jsonify({"code":500}), 500

@app.route('/device/create', methods=['POST'])
def create_device():
   # add_a device to devices
   request_data = request.get_json()
   name = request_data.get("name")
   topic = request_data.get("topic")
   device_details = request_data.get("device_details")
   if not name:
      response= {
         "status":400,
         "message": "Device name missing",
         "error_message": f"Device name = {name} not allowed"
      }
   elif not topic:
      response= {
         "status":400,
         "message": "Device topic missing",
         "error_message": f"Cannot register device with subscription topic = {topic}"
      }
   # TODO : Add check for if the topic exists
   else:
      response = add_device(name, topic, device_details)

   return jsonify(response), response["status"]


@app.route('/device/get', methods=['GET'])
def get_devices_():
   response  = get_devices()
   return jsonify(response), response["status"]

@app.route('/device/get/<id>', methods=['GET'])
def get_device_by_id_(id):
   response = get_device_by_id(id)   
   return jsonify(response), response["status"]

@app.route('/recording/get', methods=['GET'])
def get_recordings_():
   response  = get_recordings()
   return jsonify(response), response["status"]

@app.route('/recording/get/<id>', methods=['GET'])
def get_recording_by_id_(id):
   print(id)
   response = get_recording_by_id(id)   
   return jsonify(response), response["status"]

