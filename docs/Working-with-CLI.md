MPD-Kit Python package comes with `mpd-cli` command. This article will tell you how to use it.

MPD-CLI is a tool to control your project and start builds. You can quickly get a list of available commands using `mpd-cli --help`.

All commands below need to be executed in project directory.

## Configuration validating

If you want to check is your configuration correct, you can execute:

`mpd-cli validate`

If your configuration is correct, you will also get an information about your project, for example:

```
Display Name: MPD-Kit
Version: 0.1.1
Description: Useful tool for projects building automatization
Entry File: src/mpd_kit/cli.py
```

If it's not, `mpd-cli` will tell you where you did a mistake. Read [DOTMPD File](dotmpd-file.md) article to learn more about filling configuration file.

## Starting build

If your project is ready for build with default arguments, just execute:

`mpd-cli letsgo`

By default, after compiling is done, MPD-Kit will copy compiled binaries to `mpd-dist` folder.

Note that some environmetns might require different settings. If you need to modify them, read article part below about `letsgo` additional arguments

### Changing Python executable path

Default Python executable path is `python3`. If you need to use another, you can add this argument to your command:

`--pythoncmd <path-to-python-executable>` or its short version: `-p <path-to-python-executable>`

### Changing `mpd-dist` folder path

As you already know, by default, MPD-Kit copies ready executable files to `mpd-dist` directory. If you need to change it, add:

```
--distdir <path-to-dist-dir>
```

or:

```
-d <path-to-dist-dir>
```

### Using certain virtual environment instead of creating new for every build

Before compiling, MPD-Kit creates an empty virtual environment, switch to it and install needed libraries. If this process takes a lot of time for you, you may specify another virtual environment name. If you did, MPD-Kit will create new venv once and use it for next builds.

```
--venv <path-to-venv>
```

or

```
-v <path-to-venv>
```