#!/usr/bin/python
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(24) == 1:
        print("front button pressed")
        publish.single("protosystem/door/1/ring", "", hostname="test.mosquitto.org")
        time.sleep(2)

GPIO.cleanup()
