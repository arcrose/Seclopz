from typing import Callable, Dict

import click

import cmd
from nli.command import CmdError


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


def main():
    command = cmd.new_hire([
        'https://mana.mozilla.org/wiki/display/SECURITY/'\
                'InfoSec+New+Hire+First+Steps'
    ])

    try:
        output = command.execute('is there a guide for new hires?')
        print(output)
    except CmdError as ex:
        print('Failed to execute.')
        print(ex)


if __name__ == '__main__':
    main()
