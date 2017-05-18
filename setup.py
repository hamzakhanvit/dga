from distutils.core import setup

setup(name='dga',
      version='1.0',
      description='Diploid genome assembler',
      author='Hamza Khan',
      author_email='hamza.khan@alumni.ubc.ca',
      packages=['dga'],
      package_dir={'dga': 'src'},
      long_description=open('README.md').read(),
     )
