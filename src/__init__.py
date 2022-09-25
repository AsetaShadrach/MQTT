from src.configs import (
    MQTT_BROKER_PORT,
    MQTT_BROKER_URL,
    MQTT_KEEPALIVE,
    app, client
)
from src.helpers import (    
    on_connect,
    on_message,
    on_log
)
# Having routes here prevents circular imports error
from src import routes

client.on_connect = on_connect
client.on_message = on_message
client.on_log= on_log
client.connect(host=MQTT_BROKER_URL,port=int(MQTT_BROKER_PORT),keepalive=MQTT_KEEPALIVE)
client.loop_start()
