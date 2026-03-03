import os
import sys
from corelibs.classes.Configuration import Configuration

def parse_config(project='.'):
    dotmpd_file = f'{project}/DOTMPD'
    if not os.path.exists(dotmpd_file):
        print('There is no DOTMPD file in your project.', file=sys.stderr)
        sys.exit(1)

    file = open(dotmpd_file, mode='r', encoding='utf-8')
    content = file.read()
    file.close()

    lines = content.split('\n')
    if len(lines) < 1 or lines[0] != 'DOTMPD1':
        print('Your DOTMPD file beginning is incorrect.', file=sys.stderr)
        sys.exit(1)
        # TODO: call exception instead of quitting program

    result = Configuration()
    for line_raw in lines[1:]:
        line = line_raw.lstrip().rstrip()
        if line == '': continue
        if line[0] == '#': continue

        key, value = line.split('>')
        result.setValue(key, value)

    result.validateRequired()
