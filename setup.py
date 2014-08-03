from ltcrabbit import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ltcrabbit',
    version=__version__,
    author='Jaromir Fojtu',
    author_email='jaromir.fojtu@gmail.com',
    url='https://github.com/syntaxsugar/ltcrabbit',
    py_modules=['ltcrabbit'],
    license='BSD',
    description='LTCRabbit.com API wrapper',
    long_description=open('README.md').read(),
    install_requires=['requests'],
)
