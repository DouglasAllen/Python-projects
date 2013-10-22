from distutils.core import setup
import tempdga
setup(name='tempdga',
      version='1.0',
      # py_modules = ['fahrenheit2celsius,fahrenheit2kelvin,__init__'],
      packages=['tempdga'],      
      author = 'Douglas G. Allen',
      author_email = 'kb9agt@gmail.com',
      url = 'http://douglasallen.github.io/gh-pages/aboutme2/',
      description = 'Converts Fahrenheit degrees to Celcuis degrees or Kelvin',
      classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
    ],
      )
