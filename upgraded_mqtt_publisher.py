import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT Broker settings
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "Yetunde/IoT/light"   # Updated topic

# Create MQTT client (updated API version to remove warning)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Callback when connected
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

client.on_connect = on_connect

# Connect to broker
client.connect(BROKER, PORT, 60)

# Start loop
client.loop_start()

try:
    while True:
        # Simulated sensor data
        temperature = round(random.uniform(20, 35), 2)
        humidity = round(random.uniform(40, 80), 2)
        light = round(random.uniform(100, 1000), 2)

        # Create JSON payload
        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "light": light,
            "unit_temp": "C",
            "unit_humidity": "%",
            "unit_light": "lux"
        }

        # Publish message
        client.publish(TOPIC, json.dumps(payload))

        print(f"Published: {payload}")

        time.sleep(5)

except KeyboardInterrupt:
    print("Stopping publisher...")
    client.loop_stop()
    client.disconnect()