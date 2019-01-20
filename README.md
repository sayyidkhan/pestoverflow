# pestoverflow
An IOT pest detector which aims to do pest analysis around your home

## Slides Link

* https://drive.google.com/open?id=1kFcdvhT4vB6llclgC1PFCr38I8kxhPC2GimvHeIzSAA

## Inspiration

- inspired from stack overflow(a website for to help you debug your programming problems)
- we came out with the idea pest overflow(an IOT device which help to debug your pest problems at home)

## Logo Inspiration

- We are so good at detecting the pest that the roaches overflow from the dustbin. 

## Marketing statement

with rising humidity and global warming more and more pest is coming to your home, how do you sleep at
night knowing that there are scary creatures lurking around your home.
**Fear not**, pest overflow is like your real life ghostbusters that aims to detect the level of pest u have at your
home.

* you still have to call your own pest exterminator after that.
 
## What it does

**Pest Overflow(product name)** is a realtime pest detection tool.

_**(1) It helps to detect pest using a motion sensor**_

_Source Code from Twilio_
![source code twilio api](https://user-images.githubusercontent.com/22993048/51434834-c1042780-1ca4-11e9-8b4a-be107391b97a.png)

_**(2) once detected, it will take an image of the pest, showing its last location**_

_Autentication Successful on Raspberry Pi_
![successful send](https://user-images.githubusercontent.com/22993048/51434842-eb55e500-1ca4-11e9-8dea-5d819897cd33.png)

_**(3) An sms is being sent out to the user to update there is a pest at home**_

_Mobile Phone Home Notification_
![mobilephone_1_edited](https://user-images.githubusercontent.com/22993048/51434911-d5e1ba80-1ca6-11e9-9027-a760f263073a.jpg)

_Messaged Received on Iphone_
![mobilephone2_edited](https://user-images.githubusercontent.com/22993048/51434919-07f31c80-1ca7-11e9-8476-bab8cd574c01.jpg)

* * user can take action to exterminate the pest or call for pest exterminator after that.**

## How I built it

_**Hardware**_
- we used the raspberry pi 3, where we house all the IOT sensors on it
- we used the raspberry pi camera, to take an image of the last location of the pest
- we used the PIR Sensor(motion sensor), to detect the pest moving around the house
- we used an Led Sensor, to have a feedback mechanism that the PIR sensor is working

_**Software**_
- We used python 3 to write the logic for the pest detector
- We used twilio API for update the user, when there is a pest

## Challenges I ran into

- We had the challenge of making the machine learning pest detection work on the raspberry pi.
- we had the challenge of using the twilio API because it was free, we can only send text messages
  for the trial version and unable to send an MMS of the image.

## Accomplishments that I'm proud of & what i have learnt

- It is our first time working with the raspberry pi and using the sensors in the hackathon.
- It is also our first experience building and connecting the API to the raspberry pi.

## What's next for AP - Pest Overflow
To build a robo exterminator, to catch the bugs
