import click

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

if __name__ == '__main__':
    seclopzbot()
