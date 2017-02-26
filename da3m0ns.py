#!/usr/bin/python
# Made by Cristian Samaniego and Mitzi Cubedo on Feb 25th, 2017
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, True)
print "sapnu puas"
time.sleep(0.2)
GPIO.output(27, False)
GPIO.cleanup()


