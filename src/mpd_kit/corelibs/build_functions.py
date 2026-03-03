from mpd_kit.classes.exceptions.SystemCommandFailed import SystemCommandFailed
import os
import shutil

def run_command(command: str):
    status = os.system(command)
    if status != 0:
        raise SystemCommandFailed([command, status])

def recreate_dir(name: str):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.mkdir(name)

def clear_dir(name: str):
    if os.path.exists(name):
        shutil.rmtree(name)