from setuptools import setup, Command
import subprocess
import os

class CustomBuild(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        # Get the 6sV2.1 directory on the platform
        cwd = os.getcwd()
        rel_path = '6sV2.1'
        abs_path = os.path.abspath(os.path.join(cwd, rel_path))
        os.chdir(abs_path)

        # Run the make command
        subprocess.check_call(['/usr/bin/make', '-f', 'Makefile', 'sixs'])

setup(
    name='6S_json',
    version='0.1',
    description='Python wrapper for 6sV2.1',
    cmdclass={'build': CustomBuild},
)
