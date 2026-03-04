# MPD-Kit

Welcome to MPD-Kit official repository!

MPD stands for "Multi-Platform Development" and solves a lot of problems that can happen while you're compiling your application.

This program is on development stage right now. If you want to support development, please give this project a star :)

[Read a documentation here!](docs/MPD-Kit Overview.md)

## Quick overview

MPD-Kit is useful tool to automate compiling Python code with `pyinstaller`. Compilation process looks like using Meson, CMake and tools like these.

First, MPD-Kit will create a virtual environment for project build and install required libraries from requirements.txt.
After installation is done, builder starts the `pyinstaller` command for files that you specified in your config file.

The latest step is copying binary files from cache to `dist` - and process is done!

## About MPD-Clicks

MPD-Clicks is the GUI application that allows you to use the same functions as from MPD-CLI with more intuitive way than MPD-CLI.
You can look at this project at https://github.com/VladosNX/MPD-Clicks

## Installing MPD-Kit

First you need to have Python 3 installed on your computer. Go to https://python.org if you don't. Then run a command below:

`pip install mpd-kit`

## Future features

### 1. Cross-compiling

Since `pyinstaller` can't cross-compile applications, MPD-Kit will solve this problem with simple and minimalistic virtual machines.
Program will copy your project source files into required VM and start cross compilers there and copy files to certain folder.
