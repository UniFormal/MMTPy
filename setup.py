from setuptools import setup, find_packages

setup(name='MMTPy',
      version='0.0.2',
      description='MMT Python API',
      url='https://github.com/UniFormal/MMTPy',
      author='Tom Wiesing',
      author_email='t.wiesing@jacobs-university.de',
      license='MIT',
      packages=find_packages(exclude=["test"]),
      install_requires=[
            'requests',
            'lxml',
            'case_class'
      ])
