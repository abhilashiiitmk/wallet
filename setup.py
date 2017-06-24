import sys
from setuptools import setup
from batua import __version__
__version__ = list(map(str, __version__))

setup(name='batua',
      version='.'.join(__version__),
      description='Customized Blockchains',
      url='http://github.com/abhilashiiitmk/wallet',
      author='Abhilash',
      author_email='enlightmeabhi@gmail.com',
      license='MIT',
      packages=['batua'],
      include_package_data=True,
      install_requires=['ecdsa', 'pycrypto'],
      entry_points={'console_scripts': ['batua=batua.cli:main']},
      keywords=['batua'],
      zip_safe=False)
