from os import name
from subprocess import call

def clear() -> int:
    cmd = 'clear' if name == 'posix' else 'clear'
    return call(cmd, shell=True)