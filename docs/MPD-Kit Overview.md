# Welcome to MPD-Kit documentation!

We're happy to see you here. Before you can start working with MPD-Kit, let us tell you what it is.

MPD-Kit (Multi-Platform-Development) is a program that allows you to automate project building for programming languages like Python. For example, if your project have multiple .py files and you don't want to write build command every time again, you can just use MPD-Kit instead.

## MPD-Kit Tools

MPD-Kit has a multiple tools that you can you while working with it. First, and neccessary one is called `MPD-CLI`. Use it to control your project builds and project managing - for example, `mpd-cli letsgo` command will start compiling with default configuration.

Second tool that can make working with MPD-Kit more intuitive and simple is MPD-Click. This is GUI-Application that allows you to contol your project even if you don't how what commands to run. This program has build-in configuration file editor (and it's called `DOTMPD`), control panel to start compiling and manage project builds.

## How it works

The first step in starting building a Python project is creating a new separate virtual environment for compiling project. MPD-Kit switches to it and starts installing libraries from your requirements.txt file. After installation is done, MPD-Kit starts compiling each file that specified in configuration file. You can edit compile command in configuration file.

You may also specify your own virtual environment path to skip creating new one and save a few minutes. If virtual environment with specified name doesn't exist, MPD-Kit will create it.

## Preparing your project for working with MPD-Kit

All you need to have is `DOTMPD` file in your project. [Read more about it](DOTMPD File.md)

