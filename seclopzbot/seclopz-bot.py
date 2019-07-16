import os
from queue import Queue
import time
from threading import Thread
from typing import Callable, Dict

import click
from flask import Flask, request
import slack

import bot


cfg = bot.Config.load(os.environ.get('SECLOPZ_CONFIG', './config.json'))
app = Flask('seclopzbot')
slack_bot = bot.Bot(os.environ['SLACK_TOKEN'], cfg)
message_queue = Queue()
terminate_signal = Queue(maxsize=1)


def respond_to_messages():
    slack_client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    for channel in slack_bot.channels_to_join():
        slack_client.channels_join(name=channel)

    try:
        while terminate_signal.empty():
            print('Inside respond_to_messages main loop')
            if not message_queue.empty():
                message = message_queue.get()
                response = slack_bot.respond_to_message(message)
                slack_client.chat_postMessage(
                        channel=response.channel,
                        text=response.message)
            
            time.sleep(0.25)
    except KeyboardInterrupt:
        print('Exiting respond_to_messages')
        return



@app.route('/', methods=['POST'])
def bot_webhook():
    if 'challenge' in request.json:
        return request.json['challenge']

    print(request.json)
    return 'Ok'


if __name__ == '__main__':
    bot_thread = Thread(target=respond_to_messages)
    bot_thread.start()
    try:
        app.run()
    except KeyboardInterrupt:
        terminate_signal.put(True)
        bot_thread.join()
