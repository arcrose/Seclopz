from typing import Callable, Dict

import click

from nli import Command, Parser, Transition


@click.group()
def seclopzbot():
    pass

@seclopzbot.command()
def cmd1():
    '''Command on seclopzbot'''
    click.echo('seclopzbot cmd1')

@seclopzbot.command()
def cmd2():
    '''Command on seclopzbot'''
    click.echo('seclopzbot cmd2')



def log_args_and_return(value: str) -> Callable[[Dict[str, str]], str]:
    def callback(args):
        print(args)
        return value

    return callback


def main():
    command = Command(
        name='hello-world',
        help='A simple test command that returns "Hello, world"',
        format='hello world',
        callback=log_args_and_return('Hello, world'),
        parser=Parser(
            start='start',
            end='world',
            transitions=[
                Transition(fr='start', to='hello', match='hello'),
                Transition(fr='hello', to='world', match='world'),
                Transition(fr='hello', to='niceties', match='.*', param='n'),
                Transition(fr='niceties', to='world', match='world')
            ]
        ))

    try:
        output = command.execute('hello beautiful world')
        print(output)
    except Exception as ex:
        print('Failed to execute.')
        print(ex.message)


if __name__ == '__main__':
    main()
