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

def main():
    command = Command(
        name='hello-world',
        help='A simple test command that returns "Hello, world"',
        format='hello world',
        callback=lambda _: 'Hello, world',
        parser=Parser(
            start='start',
            end='world',
            transitions=[
                Transition(fr='start', to='hello', match='hello'),
                Transition(fr='hello', to='world', match='world')
            ]
        ))

    try:
        output = command.execute('hello world')
        print(output)
    except:
        print('Failed to execute')


if __name__ == '__main__':
    main()
