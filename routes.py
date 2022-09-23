from flask import request,jsonify 
from src import app

# Check if this thing is up
@app.route("/")
def hello():
    return "Hi there! Service is up."

@app.route('/publish', methods=['POST'])
def publish_message(mqtt_client):
   request_data = request.get_json()
   publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
   return jsonify({'code': publish_result[0]})

@app.route('/device/get', methods=['GET'])
def get_records1(request):
   print(request)
   return jsonify({'code': 0})

@app.route('/recording/get', methods=['GET'])
def get_records2(request):
   print(request)
   request_data = request.get_json()
   return jsonify({'code': request_data})

@app.route('/device/create', methods=['POST'])
def get_records3():
   print(request)
   request_data = request.get_json()
   return jsonify({'code': request_data})

