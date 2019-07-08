'''Exports a `Command` class that describes commands that Seclopzbot is capable
of processing.
'''

from dataclasses import dataclass, field
from typing import Callable, Generic, List, Optional, TypeVar

from nli.parser import Parser


E = TypeVar('E', bound=Exception)  # Generic type that subclasses `Exception`.


@dataclass
class CmdError(Exception, Generic[E]):
    '''An `Exception` type that indicates that a callback invocation failed.
    '''

    message: str
    cause: Optional[E] = field(default=None)


@dataclass
class Command:
    '''Represents a command that the bot can process.

        * `name` is an arbitrary but preferably kebab-case name to list in help
        messages.
        * `help` is a string that describes what the command does to Slack users.
        * `format` describes the expected input format using the conventions
        defined in [The NLI doc](seclopzbot/docs/nli.md#documentation).
        * `callback` is a function that will be called with all parsed parameters
        and is expected to return a string message to write back to Slack.
        * `parser` is a description of the deterministic pushdown automaton (DPDA)
        that parses input conforming to the expected format for the command.
    '''

    name: str
    help: str
    format: str
    callback: Callable[[List[str]], str]
    parser: Parser


    def execute(self, input_str: str) -> str:
        '''Parse an input string to execute a command's callback with any
        extracted parameters.
        '''

        args = self.parser.parse(input_str)

        try:
            return self.callback(args)
        except Exception as cause:
            raise CmdError(
                f'Callback invocation with arguments {args} failed.',
                cause)
