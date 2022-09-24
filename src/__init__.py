from src.helpers import (
    client, 
    on_connect,
    on_message
)
from src.configs import (
    MQTT_BROKER_PORT,
    MQTT_BROKER_URL
)

client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER_URL)
client.loop_start()
