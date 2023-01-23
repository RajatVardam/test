from setuptools import setup

setup(
   name='rajat',
   version='1.0',
   description='A useful module',
   author='Rajat Vardam',
   author_email='foomail@foo.example',
   packages=['Rajat'],  #same as module name
   install_requires=[], #external packages as dependencies
    classifiers=[
        "Development Status :: Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)