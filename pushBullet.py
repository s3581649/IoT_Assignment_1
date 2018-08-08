#!/usr/bin/env python3
import requests
import json
import os

NOOR_ACCESS_TOKEN="o.48V7vRrcHLNV549ExODgrb4aHDnPlVNx" 
NICK_ACCESS_TOKEN="o.gEW30Z02572UH5euayScYtzSdpO1T9hr"


def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + NOOR_ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error: Message was not sent :(')
    else:
        print('Message was sent!')