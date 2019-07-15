from typing import Optional

from bot import Config
import cmd
from nli.command import CmdError
from nli.parser import ParseError


_INVALID_CMD = 'I didn\'t understand your command, sorry.\n'\
        'Please try asking for help with "seclopzbot help"'


class Bot:
    '''The main interface into the set of commands supported by Seclopz-bot.
    '''

    def __init__(self, token: str, conf: Config):
        self.slack_token = token
        self.configuration = conf
        self._commands = [
            cmd.new_hire(self.configuration.new_hire_links)
        ]


    def respond_to_message(self, msg: str) -> Optional[str]:
        '''Determine if a message invokes any of the commands registered to the
        bot, returning the output of the first successfully invoked command.
        '''

        for command in self._commands:
            try:
                return command.execute(msg)
            except CmdError:
                continue
            except ParseError:
                continue

        return _INVALID_CMD

