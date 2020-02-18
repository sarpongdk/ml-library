#/usr/bin/env python3

import setuptools

# long description
longDesc = ""
with open("README.md", "r") as f:
   longDesc = f.read()

# parsing requirements.txt
requirements = []
with open("requirements.txt", "r") as fr:
   for line in fr:
      requirements.append(line.strip())

# setup tools
setuptools.setup(name='pyml',
      version='0.0.1',
      description='A machine learning library developed for personal use. This library evolved from my desire to understand the low level details of popular machine learning models and techniques. As such it has been solely implemented in python 3'
      author='David Sarpong',
      author_email='sarpong.david2@gmail.com',
      long_description=longDesc,
      long_description_content_type="text/markdown",
      python_requires="~3.*.*",
      url='https://github.com/sarpongdk/ml-library',
      packages=setuptools.find_packages(),
      install_requires=requirements,
      classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent"
      ]
    )

