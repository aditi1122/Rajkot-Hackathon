#!/usr/bin/env python
from time import gmtime, strftime
import fingerpi as fp
# from fingerpi import base
from twilio.rest import Client
# import struct
import time
# import matplotlib.pyplot as plt
import pickle


def printByteArray(arr):
    return map(hex, list(arr))

f = fp.FingerPi()

print 'Opening connection...'
f.Open(extra_info = True, check_baudrate = True)

print 'Changing baudrate...'
f.ChangeBaudrate(115200)
# f.CmosLed(False)

while True:
    print 'Place the finger on the scanner and press <Enter>'
    _ = raw_input()
    f.CmosLed(True)
    # response = f.IsPressFinger()
    response = f.CaptureFinger()
    if response[0]['ACK']:
        break
    f.CmosLed(False)
    if response[0]['Parameter'] != 'NACK_FINGER_IS_NOT_PRESSED':
        print 'Unknown Error occured', response[0]['Parameter']
        
# print f.UsbInternalCheck()
        
print 'Image captured!'
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
f.CmosLed(False)

print 'Transmitting image...'
# the following line needs your Twilio Account SID and Auth Token
client = Client("AC180a5165576063b3b4cb480943e476c2", "c265ff2fb936e7e8e4cf01b4421d97dd")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number

client.messages.create(to="+917769986774",  from_="+12244707905",body="Hi , You have successfully reached the office at :"+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
t = time.time()
raw_img = f.GetImage()
tx_time = time.time() - t
# print raw_img[0]['ACK'],
# print raw_img[1]['Checksum']
print 'Time to transmit:', tx_time

print 'Closing connection...'
f.Close()

with open('raw_img.pickle', 'w') as f:
    pickle.dump(raw_img, f)

# f = figure()
# f.imshow()
