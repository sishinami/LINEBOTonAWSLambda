from __future__ import print_function
import requests
import json
import os
import logging

print('Loading function')

# ref https://devdocs.line.me/ja/#reply-message
REQUEST_URL = 'https://api.line.me/v2/bot/message/reply'

REQUEST_HEADERS = {
  'Authorization': 'Bearer ' + os.environ['ACCESS_TOKEN'],
  'Content-type': 'application/json'
}


def lambda_handler(event, context):
  print(event)
  print(context)
  body = json.loads(event['body'])
  for event in body['events']:
    reply_token = event['replyToken']
    message = event['message']
    body = {
        "replyToken": reply_token,
        "messages" : [{
            "type" : "text",
            "text" : message['text']
            }]
        }

    response = requests.post(REQUEST_URL, headers=REQUEST_HEADERS, data=json.dumps(body))
    print(response)

