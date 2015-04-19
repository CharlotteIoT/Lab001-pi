import paho.mqtt.client as mqtt
import subprocess
import time

mode = 'unknown'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("protosystem/door/+/ring")
	client.subscribe("protosystem/security/mode")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	global mode
	print mode
	print(msg.topic+" "+str(msg.payload))
	if '/ring' in msg.topic:
		if mode == 'stay':
			print('silent doorbell')
		if mode == 'disarmed' or mode == 'away' or mode == 'unknown':
			filenamering1 = r'../Media/doorbell-1.wav'
			subprocess.Popen([ "/usr/bin/aplay", '-q', filenamering1 ] )	
		if mode == 'away':
			time.sleep(2)
			filenamering1 = r'../Media/dog_bark4.wav'
			subprocess.Popen([ "/usr/bin/aplay", '-q', filenamering1 ] )	
	if '/mode' in msg.topic:
		mode=str(msg.payload)
		print mode

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()