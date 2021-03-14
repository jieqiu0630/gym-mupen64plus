from setuptools import setup

setup(name='gym_mupen64plus',
      version='0.0.3',
      install_requires=['gym',
                        'numpy',
                        'PyYAML',
                        'termcolor',
                        'mss', # 4.0.3 removes support for Python 2.7
                        'opencv-python'])
