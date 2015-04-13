#!/usr/bin/env python

from time import sleep  # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO # Allows us to call our GPIO pins and names it just GPIO
import emailer
 
GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 5      # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
GPIO.setup(INPUT_PIN, GPIO.IN)  # Set our input pin to be an input

# Create a function to run when the input is high
print('Ericsson connected post box is running and waiting for post...');

def inputLow(channel):
    emailer.sendTo("nomanlatif@gmail.com");
    print('Received new post and email has been sent to recipient');
    sleep(2); # Sleep for 2 seconds so we do not send lot of emails.
    
GPIO.add_event_detect(INPUT_PIN, GPIO.FALLING, callback=inputLow, bouncetime=200) # Wait for the input to go low, run the function when it does

# Start a loop that never ends
#while True:
#    print('3.3');
#    sleep(1);           # Sleep for a full second before restarting our loop
