from __future__ import print_function
import requests
import json
import os
import logging

print('Loading function')

# ref https://devdocs.line.me/ja/#reply-message
REQUEST_URL = 'https://api.line.me/v2/bot/message/reply'

REQUEST_HEADERS = {
  'Authorization': 'Bearer ' + os.environ['ENTER_ACCESS_TOKEN'],
  'Content-type': 'application/json'
}


def lambda_handler(event, context):
  print(event)
  print(context)
  body = json.loads(event['body'])
  for event in body['events']:
    reply_token = event['replyToken']
    message = event['message']

    body = '{"replyToken":"%s" ,"messages":[{"type":"text","text":"Hello, user"},{"type":"text","text":"May I help you?"}]}' % reply_token

    response = requests.post(REQUEST_URL, headers=REQUEST_HEADERS, data=body)
    print(response)

