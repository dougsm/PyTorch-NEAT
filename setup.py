from setuptools import setup

setup(name='pytorch_neat',
      version='0.1',
      description='Pytorch NEAT',
      url='http://github.com/uber-research/PyTorch-NEAT',
      author='Uber',
      install_requires=[
        'neat-python',
        'numpy',
        'click',
        'torch'
          ],
      packages=['pytorch_neat'],
      )
