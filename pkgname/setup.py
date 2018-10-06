from setuptools import setup

with open('requirements.txt') as f:
  reqs = list(f.read().strip().split('\n'))

setup(install_requires=reqs)
