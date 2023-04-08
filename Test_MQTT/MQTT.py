import paho.mqtt.publish as publish

# Set MQTT broker address and topic
MQTT_BROKER_ADDRESS = "192.168.1.176"
MQTT_TOPIC = "UPSHat/topic"

# Set message payload
message = "Hello, MQTT!"

# Publish message to broker
publish.single(MQTT_TOPIC, message, hostname=MQTT_BROKER_ADDRESS)