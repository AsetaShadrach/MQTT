from src.helpers import (
    client, 
    MQTT_BROKER_URL,
    on_connect,
    on_message
)

client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER_URL)
client.loop_start()
