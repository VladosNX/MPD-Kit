import os
from corelibs.classes.exceptions.SystemCommandFailed import SystemCommandFailed

def run_command(command):
    status = os.system(command)
    if status != 0:
        raise SystemCommandFailed([command, status])