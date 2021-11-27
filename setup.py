import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sim900-http',  
     version='0.0.1',
     author="Soumojit Ash",
     author_email="soumojitash@gmail.com",
     description="A Python Library for easy HTTP communication using SIM900/800 module",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Soumojit28/sim900-http",
     include_package_data=True,
     packages=setuptools.find_packages(),
     install_requires=[],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )