from setuptools import setup, find_packages

setup(name='MMTPy',
      version='0.0.1',
      description='MMT Python API',
      url='https://gl.mathhub.info/ODK/MMTPy',
      author='Tom Wiesing',
      author_email='t.wiesing@jacobs-university.de',
      license='MIT',
      packages=find_packages(exclude=["test_*"]),
      install_requires=[
          'requests',
          'lxml'
      ])
