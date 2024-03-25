from setuptools import setup

setup(
    name='analyzeMFT',
    version='3.0.1',
    author='David Kovar',
    author_email='dkovar@gmail.com',
    packages=['analyzemft'],
    url='https://github.com/CarlosGTrejo/analyzeMFT',
    license='LICENSE.txt',
    description='Analyze the $MFT from a NTFS filesystem.',
    long_description=open('README.txt').read(),
    entry_points = {
        'console_scripts': [
            'analyzeMFT = analyzemft.__main__:main'
        ]
    }
)
