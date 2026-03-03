from mpd_kit.corelibs.classes.Configuration import Configuration
from mpd_kit.corelibs.classes.exceptions.SystemCommandFailed import SystemCommandFailed
from mpd_kit.corelibs.classes.BuildArguments import BuildArguments
import mpd_kit.corelibs.configparse.parser as configparser
import mpd_kit.corelibs.build_functions as build_functions
import mpd_kit.vars as vars
import os
import shutil

class Project:
    path = '.'
    config = Configuration()

    def __init__(self, path):
        self.path = path

        config = configparser.parse_config(self.path)

    def build(self, log, next_step, arguments: BuildArguments):
        # progress_funcs should accept 2 arguments - category and info
        # category is a type of information - info, warn, done, error, cmd
        log('info', f'Running MPD-Kit {vars.VERSION}, task: letsgo')
        python_cmd = 'python3' if arguments.python_cmd is None else arguments.python_cmd
        venv_path = 'mpd-venv'
        log('info', f'Using {python_cmd} as Python executable')
        log('info', f'Using {venv_path} as Python virtual environment')

        # Step 1: Creating virtual environment
        next_step(1, 'Creating virtual environment')
        try:
            build_functions.run_command(f"{python_cmd} -m venv {venv_path}")
        except SystemCommandFailed:
            log('error', f'Failed to create a virtual environment')
            return False
        log('done', 'Virtual environment created successfully')

        old_path = os.environ['PATH']
        log('info', f'Old PATH: {old_path}')
        new_path = f"{os.path.abspath(self.path)}/{venv_path}/bin:{old_path}" # TODO: make this program working with absolute venv_path correctly
        os.environ['PATH'] = new_path
        log('info', f'New PATH: {new_path}')
        log('done', f'Switched to virtual environment')

        # Step 2: Installing libraries
        next_step(2, 'Installing libraries')
        if os.path.exists(f'{os.path.abspath(self.path)}/requirements.txt'):
            try:
                build_functions.run_command('pip install -r requirements.txt')
            except SystemCommandFailed:
                log('error', 'Failed to install libraries from requirements.txt')
                return False
        else:
            log('warn', 'There is no requirements.txt, skipping libraries installation')

        log('info', 'Installing pyinstaller')
        try:
            build_functions.run_command('pip install pyinstaller')
        except SystemCommandFailed:
            log('error', 'Failed to install pyinstaller')
            return False

        log('done', 'All libraries installed successfully')

        # Step 3: Compiling
        next_step(3, 'Compiling')
        builddir = os.path.join(os.path.abspath(self.path), 'mpd-files')
        build_functions.recreate_dir(builddir)
        log('done', f'Created directory "{builddir}"')

        entries = self.config.getRecurringValues('ENTRY')
        for file in entries:
            log('info', f'Compiling {file}')
            baseflags = self.config.getValue("BASEFLAGS")
            baseflags = '' if not baseflags else baseflags
            installation_command = f'cd {builddir} && pyinstaller -F {baseflags} ../{file}'
            log('cmd', installation_command)
            try:
                build_functions.run_command(installation_command)
            except SystemCommandFailed:
                log('error', f'Failed to compile {file}')
                return False
            log('done', f'{file} compiled successfully')

        # Step 4: Copying and cleaning
        next_step(4, 'Copying and cleaning')
        result_dir = os.path.join(os.path.abspath(self.path), 'mpd-dist')
        log('info', f'Copying dist directory to {result_dir}')
        build_functions.clear_dir(result_dir)
        shutil.copytree(f'{builddir}/dist', result_dir)
        log('done', f'dist directory copied')


        shutil.rmtree(builddir)
        shutil.rmtree(venv_path)

        log('done', 'Compilation done!')

        # at the end of executing
        log('info', 'Switching back to old PATH')
        os.environ['PATH'] = old_path

        return True