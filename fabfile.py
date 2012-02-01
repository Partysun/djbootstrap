from fabric.colors import green
from fabric.api import run, env, sudo

env.hosts = ['192.168.1.33']
env.user = "partysun"

# The git origin is where we the repo is.
# Use the user@host syntax
GIT_ORIGIN = "git@github.com"

# The git repo is the repo we should clone
GIT_REPO = "partysun/djbootstrap.git"

# These are packages we need to install using APT
INSTALL_PACKAGES = [
        "python-setuptools",
        "python-pip"
        ]

def hello():
    """print hello :)"""
    print(green('\nHello world!\n'))

def uptime():
    """ Print Hello world! on remote system. """
    run('echo "Check uptime..." ')
    run('uptime')

def sub_install_packages():
    "Installs necessary packages on host"
    sudo("apt-get update")
    package_str = " ".join(INSTALL_PACKAGES)
    sudo("apt-get -y install "+package_str)

