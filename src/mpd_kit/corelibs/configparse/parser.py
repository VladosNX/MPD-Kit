import os
import sys
from mpd_kit.classes.Configuration import Configuration
from mpd_kit.classes.exceptions.UnknownValue import UnknownValue
from mpd_kit.classes.exceptions.BrokenConfig import BrokenConfig
from mpd_kit.classes.exceptions.NoConfigFile import NoConfigFile

def parse_plain(content):
    lines = content.split('\n')
    if len(lines) < 1 or lines[0] != 'DOTMPD1':
        raise NoConfigFile()

    result = Configuration()
    for line_raw in lines[1:]:
        line = line_raw.lstrip().rstrip()
        if line == '': continue
        if line[0] == '#': continue

        try:
            key, value = line.split('>')
        except ValueError:
            raise BrokenConfig()
        result.setValue(key, value)

    result.validateRequired()
    return result

def parse_config(project='.'):
    dotmpd_file = f'{project}/DOTMPD'
    if not os.path.exists(dotmpd_file):
        raise NoConfigFile()

    file = open(dotmpd_file, mode='r', encoding='utf-8')
    content = file.read()
    file.close()

    return parse_plain(content)

