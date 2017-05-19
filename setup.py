from setuptools import setup
import sys

if not sys.version_info[0] == 3:
    sys.exit("Sorry, only Python 3 is supported")

files = ["data/*"]

setup(name='dga',
      version='1.0',
      description='Diploid genome assembler',
      author='Hamza Khan',
      author_email='hamza.khan@alumni.ubc.ca',
      packages=['dga'],
      scripts=['run-dga.py'],
      install_requires=[
              'gfapy',
      ],
      package_data = {'dga' : files },
      zip_safe=False)
