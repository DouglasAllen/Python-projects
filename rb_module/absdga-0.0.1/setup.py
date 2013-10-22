from ez_setup import use_setuptools
use_setuptools()
from distutils.core import setup
setup(
    name = 'absdga',
    version = '0.0.2',
    py_modules = ['absdga'],
    author = 'rubylearning_student_dga',
    author_email = 'kb9agt@gmail.com',
    url = 'http://douglasallen.github.io/gh-pages/aboutme2/',
    description = 'Gives the absolute value of a number',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
    ],
)