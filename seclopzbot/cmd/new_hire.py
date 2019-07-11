from typing import Callable, Dict, List, Optional

from nli import Command, Parser, Transition


def new_hire(links: Optional[List[str]] = None) -> Command:
    '''Creates a `Command` that, when invoked, produces a message with links
    to useful documents for new hires to read about security practices.
    '''

    return Command(
        name='new-hires',
        help='Links to useful security information for new hires',
        format='(...) new hire[s]',
        callback=_respond(links),
        parser=Parser(
            start='start',
            end='hire',
            transitions=[
                Transition(fr='start', to='new', match='new'),
                Transition(fr='new', to='hire', match='hires?'),
                Transition(fr='start', to='arbitrary', match='.*'),
                Transition(fr='arbitrary', to='new', match='new')
            ]
        ))


def _respond(links: Optional[List[str]]) -> Callable[[Dict[str, str]], str]:
    def callback(args):
        if links is None:
            return 'There is no information available at this time. '\
                    'Please ask for assistance in #infosec.'

        return 'Here are some links that should help you get started:\n' +\
                '\n'.join(links)

    return callback
