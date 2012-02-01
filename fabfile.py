from fabric.colors import green
from fabric.api import run,  env

env.hosts = ['192.168.1.33']
env.user = "partysun"

def hello():
    """print hello :)"""
    print(green('\nHello world!\n'))

def uptime():
    """ Print Hello world! on remote system. """
    run('echo "Check uptime..." ')
    run('uptime')

