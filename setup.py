#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='goobs',
     version='0.0.1',
     description='Google Browser Search',
     author='Lars Feldeisen',
     author_email='lars@feldeisen.de',
     url='',
     license='GPLv2',
     classifiers=[
       'Development Status :: 5 - Production/Stable',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: GPLv2 License',
       'Operating System :: POSIX :: Linux',
       'Programming Language :: Python :: 2',
       'Programming Language :: Python :: 3',
    ],
      package_dir={"": "goobs"},
      packages=find_packages(
          where="goobs", 
          exclude=["contrib", "docs", "tests*", "tasks"],
        ),
      entry_points={
        "console_scripts": [
            "goobs=goobs:main"
        ],
     },
    include_package_data=True,
     )