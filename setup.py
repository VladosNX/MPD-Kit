from setuptools import setup, find_packages
from src.mpd_kit.vars import VERSION

description = open('README.md', 'r', encoding='utf-8').read()

setup(
    name="mpd_kit",
    version=VERSION,
    url="https://github.com/VladosNX/MPD-Kit",
    long_description=description,
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        "console_scripts": [
            "mpd-cli=mpd_kit.cli:main"
        ]
    }
)
