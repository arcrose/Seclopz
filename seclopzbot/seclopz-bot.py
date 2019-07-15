import os
from typing import Callable, Dict

import click
from flask import Flask, request

import bot


cfg = bot.Config.load(os.environ.get('SECLOPZ_CONFIG', './config.json'))
app = Flask('seclopzbot')
slack_bot = bot.Bot(os.environ['SLACK_TOKEN'], cfg)


@app.route('/', methods=['POST'])
def bot_webhook():
    return bot.respond_to_message(request.json['message'])


if __name__ == '__main__':
    app.run()
