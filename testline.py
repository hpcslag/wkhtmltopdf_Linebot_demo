# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
	LineBotApi, WebhookParser
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

##modify
import test #同一個目錄的 test.py
#need to use serve static
app = Flask(__name__, static_folder='static')
##modify

# get channel_secret and channel_access_token from your environment variable
channel_secret = ""#os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = "" #os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
	print('Specify LINE_CHANNEL_SECRET as environment variable.')
	sys.exit(1)
if channel_access_token is None:
	print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
	sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# parse webhook body
	try:
		events = parser.parse(body, signature)
	except InvalidSignatureError:
		print("SIGN ERR")
		abort(400)

	# if event is MessageEvent and message is TextMessage, then echo text
	for event in events:
		if not isinstance(event, MessageEvent):
			continue
		if not isinstance(event.message, TextMessage):
			continue

		
		"""try:
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text="你作業寫的怎麼樣?")
			)
		except:
			return 'OK'"""

		##modify
		try:
			basicPath = "https://fd5e8177ebea.ngrok.io/"
			p = test.searchAndGetImage(name=event.message.text)

			fullPath = basicPath + p
			
			line_bot_api.reply_message(
				event.reply_token,
				ImageSendMessage(original_content_url=fullPath, preview_image_url=fullPath)
			)
		except Exception as e: 
			print(e)
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage("ㄛㄛ......")
			)
			return 'OK'
		##modify	
		
	return 'OK'


if __name__ == "__main__":
	arg_parser = ArgumentParser(
		usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
	)
	arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
	arg_parser.add_argument('-d', '--debug', default=False, help='debug')
	options = arg_parser.parse_args()

	app.config['JSON_AS_ASCII'] = False

	app.run(debug=True, host='0.0.0.0', port=80) #line problem
