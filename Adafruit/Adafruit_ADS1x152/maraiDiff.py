#!/usr/bin/python

import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15
import htmlmodule


def signal_handler(signal, frame):
    # print 'You pressed Ctrl+C!'
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
# print 'Press Ctrl+C to exit'

ADS1015 = 0x00  # 12-bit ADC

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1015)

old = 0
while True:
    # Read channels 2 and 3 in single-ended mode, at +/-4.096V and 250sps
    volts0 = adc.readADCSingleEnded(0, 256, 8) / 1000.0
    volts1 = adc.readADCSingleEnded(1, 256, 8) / 1000.0

    # Now do a differential reading of channels 2 and 3
    voltsdiff = adc.readADCDifferential01(256, 8) / 1000.0

    if (voltsdiff == 0 and old != 0):
        #	if ((old < voltsdiff and voltsdiff < 0.001) or (old > voltsdiff and voltsdiff > 0.001)):
        print "package arrived"
        recipients = ["noman@noman.com"]
        serverUrl = "https://postbox-piinnovation.rhcloud.com/PostboxServer/api/v1/notification/notify"
        htmlmodule.sendRecipientsAsPost(recipients, serverUrl)
        print("ZZzz")
        print(serverUrl)
        time.sleep(5.0)
        htmlmodule.sendRecipientsAsPost(recipients, serverUrl)

    old = voltsdiff

    # Display the two different reading for comparison purposes
    print "%.8f %.8f %.8f %.8f" % (volts0, volts1, volts1 - volts0, -voltsdiff)
    time.sleep(1)
