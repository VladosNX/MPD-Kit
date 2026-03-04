import mpd_kit.vars as vars
import sys
import mpd_kit.argparser.argparse as argparse
from mpd_kit.classes.Project import Project
from mpd_kit.classes.BuildArguments import BuildArguments

def show_log(category, info):
    colors = {
        'info': 4,
        'warn': 3,
        'error': 1,
        'done': 2,
        'cmd': 5
    }

    print(f"[\x1b[3{colors[category]}m{category.ljust(5)}\x1b[0m] {info}")

def show_step(step, title):
    print(f'+===== STEP {step}')
    print(f'| {title}')
    print(f'+===========')

def main():
    arguments = argparse.parse(sys.argv)

    if arguments['help']:
        print(f"MPD-Kit {vars.VERSION}")
        print("")
        print("Made by VladosNX. Follow me on my GitHub! https://github.com/VladosNX")
        print("")
        print("Basic usage:")
        print("  mpd-cli <mode> [--help]")
        print("")
        print("mode: Which action MPD-Cli has to do")
        print("--help: Show this message")
        print("--verbose: Show more information about current task")
        print("")
        print("Available modes:")
        print("")
        print("letsgo: Start compiling process with default configuration")
        print("validate: Check is your config file correct and show information about this project")
        print("")
        print("Additional options:")
        print("--pythoncmd -p <cmd>: Set Python executable file path (default is python3)")
        print("--distdir -d <dir>: Specifies where to store result files (default is mpd-dist)")
        print("--venv -v <path>: Using specified virtual environment instead of creating new")
        print("")
        print("If you have some problems with MPD-CLI, please consider creating an issue on GitHub:")
        print("  https://github.com/VladosNX/MPD-Kit/issues")
        print("or consider using MPD-Clicks instead if you prefer GUI:")
        print("  https://github.com/VladosNX/MPD-Clicks")
        sys.exit()

    project = Project('.')

    if arguments['mode'] == 'validate':
        for item in project.config.values:
            print(f"{project.config.getValueSignature(item[0]).pretty_name}: {item[1]}")
    elif arguments['mode'] == 'letsgo':
        build_arguments = BuildArguments()
        if arguments['pythoncmd']: build_arguments.python_cmd = arguments['pythoncmd']
        if arguments['distdir']: build_arguments.dist_dir = arguments['distdir']
        if arguments['venv']: build_arguments.custom_venv = arguments['venv']
        project.build(show_log, show_step, build_arguments)

if __name__ == '__main__':
    main()
