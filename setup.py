from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import pybind11

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def build_extension(self, ext):
        import subprocess
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        env = os.environ.copy()
        env['pybind11_DIR'] = pybind11.get_cmake_dir()
        subprocess.check_call(['cmake', ext.sourcedir], cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.', '--config', 'Release'], cwd=self.build_temp, env=env)

setup(
    name='ironcircuit',
    version='0.1.0',
    ext_modules=[CMakeExtension('ironcircuit')],
    cmdclass={'build_ext': CMakeBuild},
)
