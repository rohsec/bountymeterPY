import io
from os import path
from setuptools import setup, find_packages

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='bmpy',
    version=__import__('bmpy').__version__,
    description='Bounty Meter is a command-line utility tool designed for bug bounty hunters to define their bounty target for a year, maintain and keep record of their bounties on a monthly basis, and track their progress throughout the year. With Bounty Meter, you can add and subtract bounties, view your total bounties earned this year, and display an interactive stats card to visualize your progress.',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='720922',
    license='GNU Affero General Public License v3.0',
    url='https://github.com/720922/bountymeterPY',
    download_url='https://github.com/720922/bountymeterPY/archive/v%s.zip' % __import__(
        'bmpy').__version__,
    packages=find_packages(),
    install_requires=['progress'],
    classifiers=[
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'bmpy = bmpy.bmpy:main'
        ]
    },
    keywords=['recon', 'bugbounty', 'pentesting', 'utility', 'hacking']
)