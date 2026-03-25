import paho.mqtt.client as mqtt
import json

# RabbitMQ settings
BROKER = "broker.emqx.io"
PORT = 1883
USERNAME = "admin"
PASSWORD = "admin"
TOPIC = "Yetunde/IoT/Light"

# Callback when connected
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to RabbitMQ MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print("Connection failed:", rc)

# Callback when message received
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"\n📥 Received data:")
        print(f"Temperature: {payload['temperature']} °C")
        print(f"Humidity: {payload['humidity']} %")
        print(f"Light: {payload['light']} lx")
    except:
        print("Raw message:", msg.payload.decode())

# Create client
client = mqtt.Client()
#client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 5552)

client.loop_forever()