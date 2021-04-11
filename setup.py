import os
import venv

from setuptools import find_packages, setup
from setuptools.command.install import install

PROJECT_NAME = 'pytest-sample'


class Install(install):
    """ Customized setuptools install command which uses pip. """

    def run(self, *args, **kwargs):
        venv_path = PROJECT_NAME + '-venv'
        venv.create(venv_path, with_pip=True)
        venv.main()

        command = f". {venv_path}/bin/activate && " \
            "pip install -r requirements-dev.txt"

        os.system(command)

setup(
    name=PROJECT_NAME,
    version='0.0.1',
    cmdclass={
        'install': Install,
    },
    packages=find_packages(),
)
