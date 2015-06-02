#!/usr/bin/python

import time, signal, sys
from gui import *
from Adafruit_ADS1x15 import ADS1x15

def signal_handler(signal, frame):
        #print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ADS1015 = 0x00	# 12-bit ADC

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1015)

gewicht = False

# HACK: Initialize GUI without displaying it
app = QtGui.QApplication(sys.argv)
gui = Gui()


while True:
	# Now do a differential reading of channels 2 and 3
	voltsdiff = adc.readADCDifferential01(1024, 8)/1000.0

	#print "%.8f" % (voltsdiff)
	if ((voltsdiff > 0.045 or voltsdiff < 0.025) and gewicht != True):
		print "gewicht gemessen"
		gui.sendPost()
		
		gewicht = True
	elif (voltsdiff < 0.045 and voltsdiff > 0.025):
		gewicht = False

	time.sleep(1)
