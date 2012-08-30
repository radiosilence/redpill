from time import sleep
from random import random
import os, sys
import yaml
import clint
from clint import resources
from clint.textui import puts, puts_err, indent, colored, progress

VENDOR = 'Dapper Dog Studios'
PACKAGE = 'redpill'
VERSION = 0.1


def create_default_config():
    puts(colored.yellow('Config does not exist, creating...'))
    defaults = {
        'prompt': True,
        'verbose': False,
        'repos': [],
    }
    dump = yaml.dump(defaults)
    resources.user.write('config.yaml', dump)
    return dump


def load_config():
    config = resources.user.read('config.yaml')
    if not config:
        config = create_default_config()
    
    return yaml.load(config)


def save_config(config):
    resources.user.write('config.yaml', yaml.dump(config))


def refresh(repository=None):
    with indent(3, quote=':: '):
        puts('Refreshing repositories...')


def sysupgrade():
    with indent(3, quote=':: '):
        puts('Upgrading system packages...')


def install(package):
    puts("INSTALL PACKAGE")
    puts(package)


def subscribe(config, repo):
    with indent(3, quote=':: '):
        puts('Subscribing to repository...')
    with indent(1):
        puts(colored.magenta(repo))
    
        repos = config['repos']
        if repo in repos:
            puts_err(colored.red(
                'You\'re already subscribed to this repository!'))
        else:
            repos.append(repo)


def redpill(args):
    resources.init(VENDOR, PACKAGE)
    config = load_config()
    if args['-S']:
        if not (
            args['<package>']
            or args['--refresh']
            or args['--sysupgrade']
        ):
            puts(colored.red('No packages to sync, exiting...'))
            sys.exit(1)

        if args['--refresh']:
            refresh()

        if args['--sysupgrade']:
            sysupgrade()

        if args['<package>']:
            install(args['<package>'])

    elif args['--subscribe']:
        subscribe(config, args['<repository>'])

    save_config(config)