#!/usr/bin/python
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(24) == 1:
        print("front button pressed")
		# TODO change the 1 to the Door Number you were given with your Pi.
        publish.single("protosystem/door/1/ring", "", hostname="test.mosquitto.org")
        time.sleep(2)

GPIO.cleanup()
