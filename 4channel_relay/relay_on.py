#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [17]

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
#    GPIO.output(i, GPIO.HIGH)


# main loop

try:
  GPIO.output(17, GPIO.LOW)
  print ("ON")



# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()

# find more information on this script at
# http://youtu.be/WpM1aq4B8-A