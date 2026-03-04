# What is DOTMPD File

DOTMPD file stores all project settings that required to work with MPD-Kit. If your project doesn't have this file, MPD-Kit programs (like MPD-CLI or MPD-Clicks) won't determine this project as MPD-Compatible and won't be showed in project discovery results.

This documentation page will tell you how to fill this file to follow your project's needs.

# Parameters

Every DOTMPD parameter is like a variable - it has its own name and value. Here, we'll use parameters to specify some required settings for our project.

Non-Recurring and required parameters:
- Display Name (DNAME)
	 Specifies name that must be showed in project overview (e.g. MPD-Clicks project page)
- Version (VERSION)
	 Specifies version that must be showed in project overview and used for comparison
- Brief description (BRIEF)
	 Specifies project description that must be showed in project overview
- Base Compiler Flags (BASEFLAGS)
	 Specifies flags that MPD-Kit should add to compiler command

Recurring parameters:
- Entry file (ENTRY) (required at least one)
	 Specifies file that must be specified in compilation tool

# Syntax

File needs to be started with `DOTMPD1` to be determined as config file. If it doesn't, this file will be ignored by MPD-Kit, and project won't be visible in project discovery.

Note that this word can depend on MPD-Kit version you want to use.

Parameters specifies with syntax like:

```
PARAMETER>VALUE
```

Comment lines must be started with `#` symbol, example:

```
# This line will be just ignored.
```

## Examples

As you already may understand, minimal config file must look like this:

```
DOTMPD1

DNAME>Some Project with MPD-Kit
VERSION>0.1
BRIEF>Use this configuration file to test MPD-Kit abilities

# Specifying all entry files that should be compiled
ENTRY>main.py
```

You can also specify few `ENTRY` parameters. For example, if you want your project to have multiple output executables, you can write:

```
ENTRY>main.py
ENTRY>helper.py
ENTRY>daemon.py
```

If you need to change default compiler command, you can specify `BASEFLAGS` parameter.

```
# This flag will be added to pyinstaller command
BASEFLAGS>-w
```

## Validating and getting all parameters

If you need to check is your file correct or get paremeter value that you didn't specify, you can run:

```
mpd-cli validate
```

If your file is correct, for our example above you will get this output:

```
Display Name: Some Project with MPD-Kit
Version: 0.1
Brief: Use this configuration file to test MPD-Kit abilities
Entry file: main.py
Entry file: helper.py
Entry file: daemon.py
Base Compiler Flags: -w
```

Note that parameters like `COMPILER` will be showed even if you didn't specify them, because they have a default value.

If you have any mistakes in your configuration file, you will see:

```
This is not a MPD-Compatible project (Error in DOTMPD)
```

Or if you set a wrong name for `DOTMPD` file:

```
This is not a MPD-Compatible project (No DOTMPD file)
```

## What's next?

If your DOTMPD file is done, you're ready to read next documentation article - [Working with CLI](Working with CLI.md)

