from flask import request,jsonify 
from src import app
from src.helpers import (
   add_device, get_devices, get_device_by_id,
    get_recordings, get_recording_by_id
   )

# Check if this thing is up
@app.route('/')
@app.route('/home')
def hello():
    return "Hi there! Service is up."

@app.route('/publish', methods=['POST'])
def publish_message(mqtt_client):
   request_data = request.get_json()
   publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
   return jsonify({'code': publish_result[0]})

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

   return jsonify(response)


@app.route('/device/get', methods=['GET'])
def get_devices_():
   response  = get_devices()
   return jsonify(response)

@app.route('/device/get/<id>', methods=['GET'])
def get_device_by_id_(id):
   response = get_device_by_id(id)   
   return jsonify(response)

@app.route('/recording/get', methods=['GET'])
def get_recordings_():
   response  = get_recordings()
   return jsonify(response)

@app.route('/recording/get/<id>', methods=['GET'])
def get_recording_by_id_(id):
   print(id)
   response = get_recording_by_id(id)   
   return jsonify(response)


if __name__ == '__main__':
    app.run()
