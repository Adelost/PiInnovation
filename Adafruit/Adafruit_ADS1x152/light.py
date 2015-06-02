#!/usr/bin/python

import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ADS1015 = 0x00  # 12-bit ADC

gain = 6144  # +/- 6.144V
sps = 8    # 8 samples per second
comp = 1

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1015)

old = 0

while True:
	# Read channel 0 in single-ended mode using the settings above
	volt0 = adc.readADCSingleEnded(0, gain, sps) / 1000

	val = old - volt0

	if val < -1: 
		print "box opened"
	elif val > 1:
		print "box closed"

	old = volt0 

	time.sleep(1)
