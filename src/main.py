#!/usr/bin/env python

from os import _exit
from shlex import split
from time import sleep

from commands.clear import clear
from utils.typer import typer
from config import *

def main() -> None:
    for msg in message:
        print(msg)

    print('\n', 'Welcome to PyTerm@{}'.format(version))

    while True:
        prompt = '$ '
        args = input(prompt)
        args = split(args)

        cmd = args.pop(0)
        args = list(map(lambda s: s[:-1] if s[-1] == ',' else s, args))
        
        if cmd == 'clear':
            _ = clear()
            if _ != 0:
                print(f'Process failed with exit code {_}')

        elif cmd == 'help':
            print('Available shell commands are:\n')
            print('help, clear')

if __name__ == '__main__':
    try:
        print('Booting up', end='', flush=True)
        sleep(1)
        typer('...')
        print('\n')

        main()

    except KeyboardInterrupt:
        _exit(1)