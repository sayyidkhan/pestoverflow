import RPi.GPIO as GPIO
import time
import random
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #PIR

list = ["racket", "newspaper", "potato", "fire", "famous amos", "Bare Hands", "ipad"]
account_sid = '#insert account sid from twilio#'
auth_token = '#insert auth_token from twilio#'
client = Client(account_sid, auth_token)

### change the statement ###
challenge_statement = "Challenge Statement: For ultimate bravery try kill the pest with " + random.choice(list)
content = "Message: pest is detected @ location."
### change the statement ###

body_content = content + "\n" + challenge_statement
message = client.messages \
                .create(
                     body= body_content,
                     from_='#insert twilio number#',
                     to='#insert test number#'
                 )
############ to put at the top of the script ################

def printLines():
	print("Motion Detected!")
	print("auth_token Successful")
	print(message.sid)
	print("Printing Message sent:")
	print(body_content)

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            printLines()
            time.sleep(10) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
