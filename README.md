Dataforeninga
=============
[![Code Health](https://landscape.io/github/jvlomax/dataforeninga/master/landscape.png)](https://landscape.io/github/jvlomax/dataforeninga/master)
[![Build Status](https://travis-ci.org/jvlomax/dataforeninga.svg?branch=master)](https://travis-ci.org/jvlomax/dataforeninga)

This is the webpage for Tromsøstudentenes Datforening
http://dataforeninga.no


To run
=============
To install all required modules run `pip install -r requirements.txt` in the root folder.
If you don't want to install all the modules to your python installation, please use a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


If you are running windows and your're having an error installing py-bcrypt, please run `pip install wheelhouse\py_bcrypt-0.4-cp[your python 
version]-none-win32.whl` in the root directory to 
install it from a cheesewheel


Before commiting
============
Always run the tests befor commiting. To test all the tests run `nosetests` in the root folder

If you are using pycharm you can also right click the "tests" folder and select "run unittsests" to run all the tests