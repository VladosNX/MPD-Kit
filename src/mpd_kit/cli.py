import vars
import sys
import argparser.argparse as argparse
from mpd_kit.classes.Project import Project
from mpd_kit.classes.BuildArguments import BuildArguments

arguments = argparse.parse(sys.argv)

if arguments['help']:
    print(f"MPD-Kit {vars.VERSION}")
    print("")
    print("Made by VladosNX. Follow me on my GitHub! https://github.com/VladosNX")
    print("")
    print("Basic usage:")
    print("  mpd-cli <mode> [--help] [--verbose / -v]")
    print("")
    print("mode: Which action MPD-Cli has to do")
    print("--help: Show this message")
    print("--verbose or -v: Show more information about current task")
    print("")
    print("Available modes:")
    print("")
    print("letsgo: Start compiling process with default configuration")
    print("validate: Check is your config file correct and show information about this project")
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
    build_arguments.python_cmd = arguments['pythoncmd']
    project.build(
        lambda category, info: print(f"{category}: {info}"),
        lambda step, title: print(f"Step {step} - {title}"),
        build_arguments
    )