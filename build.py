import os
import shutil
import sys
import shutil

if os.path.exists('dist'): shutil.rmtree('dist')

if not os.system('python3 setup.py sdist bdist_wheel --dry-run --verbose') == 0: sys.exit(1)
if os.path.exists('src/mpd_kit.egg-info'): shutil.rmtree('src/mpd_kit.egg-info')
shutil.rmtree('build')