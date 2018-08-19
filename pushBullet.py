#!/usr/bin/env python3
"""
REFERENCE: This script was partially taken from the RMIT IoT Tute/Lab Code Archive and was slightly modified
"""
#imports requests, json and os modules
import requests
import json
import os
#initialises token for pushbullet
ACCESS_TOKEN="o.48V7vRrcHLNV549ExODgrb4aHDnPlVNx" 
#Method for running the pushbullet request and sending a message
def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN,  
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error: Message was not sent :(')
    else:
        print('Message was sent!')