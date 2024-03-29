#!/usr/bin/python

import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C to exit'

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01	# 16-bit ADC

# Select the gain
gain = 6144  # +/- 6.144V
# gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Select the sample rate
sps = 8    # 8 samples per second
# sps = 16   # 16 samples per second
# sps = 32   # 32 samples per second
# sps = 64   # 64 samples per second
# sps = 128  # 128 samples per second
# sps = 250  # 250 samples per second
# sps = 475  # 475 samples per second
# sps = 860  # 860 samples per second
#sps = 250

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1015)

while True:
	# Read channel 0 in single-ended mode using the settings above
	volt0 = adc.readADCSingleEnded(0, gain, sps) / 1000
#	volt1 = adc.readADCSingleEnded(1, gain, sps) / 1000
#	volt0 = adc.readADCSingleEnded(0)
#	volt1 = adc.readADCSingleEnded(1)
#	volt2 = adc.readADCSingleEnded(2, gain, sps) / 1000
#	volt3 = adc.readADCSingleEnded(3, gain, sps) / 1000

	# To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
	# volts = adc.readADCSingleEnded(3, 1024, 860)

#	print "0: %.6f      1: %.6f      2: %.6f      3: %.6f" % (volt0, volt1, volt2, volt3)
	#	print "1: %.6f" % (volt1)
#	print "2: %.6f" % (volts)
	print "3: %.6f" % (volt0)

	time.sleep(1)
