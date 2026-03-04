import os
import sys
from mpd_kit.classes.Configuration import Configuration
from mpd_kit.classes.exceptions.UnknownValue import UnknownValue
from mpd_kit.classes.exceptions.NoConfigFile import NoConfigFile

def parse_config(project='.'):
    dotmpd_file = f'{project}/DOTMPD'
    if not os.path.exists(dotmpd_file):
        raise NoConfigFile()

    file = open(dotmpd_file, mode='r', encoding='utf-8')
    content = file.read()
    file.close()

    lines = content.split('\n')
    if len(lines) < 1 or lines[0] != 'DOTMPD1':
        raise NoConfigFile()

    result = Configuration()
    for line_raw in lines[1:]:
        line = line_raw.lstrip().rstrip()
        if line == '': continue
        if line[0] == '#': continue

        key, value = line.split('>')
        try:
            result.setValue(key, value)
        except UnknownValue as e:
            print(f'Unknown config value {e}', file=sys.stderr)
            sys.exit(1)

    result.validateRequired()
