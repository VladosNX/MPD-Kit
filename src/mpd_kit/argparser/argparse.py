import sys
import mpd_kit.argparser.argvars as argvars
import mpd_kit.argparser.argconditions as argconditions

# Input dictionary has information about all available options.
# Options are stored in order like:
#  [ type: int, id: str, required: bool|function, short: str|None, has_value: bool, order: int|None ]
# If you specified a function to 'required' field, it will be executed after arguments parsing is done to check if argument should be required based on context
# long and short options aren't required if you didn't set type to '1'
# order is used for ordinal arguments

inputs = [
    [ argvars.TYPE_ORDINAL, 'mode', argconditions.isModeRequired, None, True, 0 ],
    [ argvars.TYPE_DOUBLEDASH, 'help', False, None, False, None ],
    [ argvars.TYPE_DOUBLEDASH, 'verbose', False, None, False, None ],
    [ argvars.TYPE_DOUBLEDASH, 'pythoncmd', False, 'p', True, None ],
    [ argvars.TYPE_DOUBLEDASH, 'distdir', False, 'd', True, None ],
    [ argvars.TYPE_DOUBLEDASH, 'venv', False, 'v', True, None ]
]

def _findByDoubleDash(value: str):
    for option in inputs:
        if option[argvars.ARG_TYPE] != argvars.TYPE_DOUBLEDASH: continue
        if value.lstrip('-') == option[argvars.ARG_ID]: return option

    return None

def _findBySingleDash(value: str):
    for option in inputs:
        if option[argvars.ARG_TYPE] != argvars.TYPE_DOUBLEDASH: continue
        if value.lstrip('-') == option[argvars.ARG_SHORT]: return option

    return None

def _findByOrdinal(index: int):
    for option in inputs:
        if option[argvars.ARG_TYPE] != argvars.TYPE_ORDINAL: continue
        if index == option[argvars.ARG_ORDER]: return option

    return None

def _findById(arg_id: str):
    for option in inputs:
        if option[argvars.ARG_ID] == arg_id: return option

    return None

def parse(args):
    ordinalIndex = 0
    options = {}
    # Filling options dictionary with zero-values
    for option in inputs:
        options[option[argvars.ARG_ID]] = None

    assignNextTo = None
    for arg in args[1:]:
        if len(arg) == 0: continue
        optionSignature = None

        if assignNextTo:
            options[assignNextTo] = arg
            assignNextTo = None
            continue

        if arg[0] == '-':
            if arg[1] == '-':
                # user specified double-dash argument
                optionSignature = _findByDoubleDash(arg)
            else:
                # user specified single-dash argument
                optionSignature = _findBySingleDash(arg)
        else:
            # user specified ordinal argument
            optionSignature = _findByOrdinal(ordinalIndex)
            ordinalIndex += 1

        if not optionSignature:
            print(f'Incorrect argument {arg} :( See --help', file=sys.stderr)
            sys.exit(1)
        elif optionSignature[argvars.ARG_TYPE] == argvars.TYPE_ORDINAL:
            options[optionSignature[argvars.ARG_ID]] = arg
        elif optionSignature[argvars.ARG_HAS_VALUE]:
            assignNextTo = optionSignature[argvars.ARG_ID]
        else:
            options[optionSignature[argvars.ARG_ID]] = True

    for option in inputs:
        if options[option[argvars.ARG_ID]] is None:
            required = False
            if option[argvars.ARG_REQUIRED] is bool and option[argvars.ARG_REQUIRED]:
                required = True
            elif callable(option[argvars.ARG_REQUIRED]):
                required = option[argvars.ARG_REQUIRED](options)

            if required:
                print(f'You skipped required argument called {option[argvars.ARG_ID]}!', file=sys.stderr)
                sys.exit(1)

    return options
