try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ltcrabbit',
    version='0.2.0',
    author='Jaromir Fojtu',
    author_email='jaromir.fojtu@gmail.com',
    url='https://github.com/syntaxsugar/ltcrabbit',
    py_modules=['ltcrabbit'],
    scripts=['bin/ltcrabbit-cli'],
    license='BSD',
    description='LTCRabbit.com API wrapper',
    long_description=open('README.md').read(),
    install_requires=['requests', 'prettytable', 'docopt'],
)
