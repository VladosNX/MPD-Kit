from setuptools import setup, find_packages
from src.mpd_kit.vars import VERSION

setup(
    name="mpd_kit",
    version=VERSION,
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)