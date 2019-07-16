from dataclasses import dataclass
from typing import List, Optional

from bot import Config
import cmd
from nli.command import CmdError
from nli.parser import ParseError


_INVALID_CMD = 'I didn\'t understand your command, sorry.\n'\
        'Please try asking for help with "seclopzbot help"'


@dataclass
class Response:
    '''Simple container for the data needed to send a message to Slack.
    '''

    channel: str
    message: str


class Bot:
    '''The main interface into the set of commands supported by Seclopz-bot.
    '''

    def __init__(self, token: str, conf: Config):
        self.slack_token = token
        self.configuration = conf
        self._commands = [
            cmd.new_hire(self.configuration.new_hire_links)
        ]


    def respond_to_message(self, msg: str) -> Optional[Response]:
        '''Determine if a message invokes any of the commands registered to the
        bot, returning the output of the first successfully invoked command.
        '''

        for command in self._commands:
            try:
                message = command.execute(msg)
                return Response(self.configuration.channels[0], message)
            except CmdError:
                continue
            except ParseError:
                continue

        return Response(self.configuration.channels[0], _INVALID_CMD)


    def channels_to_join(self) -> List[str]:
        '''Returns the configured list of channels to join.
        '''

        return self.configuration.channels
