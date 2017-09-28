# Yummy-Recipes web app without database
[![Build Status](https://travis-ci.org/geofrocker/Yummy-Recipes.svg?branch=master)](https://travis-ci.org/geofrocker/Yummy-Recipes)
[![Coverage Status](https://coveralls.io/repos/github/geofrocker/Yummy-Recipes/badge.svg?branch=master)](https://coveralls.io/github/geofrocker/Yummy-Recipes?branch=master)
![pylint Score](https://mperlet.github.io/pybadge/badges/7.29.svg)
[![Requirements Status](https://requires.io/github/geofrocker/Yummy-Recipes/requirements.svg?branch=master)](https://requires.io/github/geofrocker/Yummy-Recipes/requirements/?branch=master)
# Description
Yummy recipies is a web app built in python using flask framework
  * A user can see the available recipes
  * A user can register for membership
  * A user can login using his/her credentials
  * A user can add, edit and delete recipes
# Installation guide
  * This application has been tested with python 3.4[Python 3.4](https://www.python.org/) and [Flask 0.11](http://flask.pocoo.org/)
  * Make sure the above requirements are satisfied
  * Navigate to the project root directory and run `pip install -r requirements.txt` from command line. [Learn more a pip](https://pypi.python.org/pypi/pip) if you don't have it already installed
  * Run `python app.py` from command line or terminal
  * You should be able to see something similar to this
  ![A screen shot of flask running in cmd](/github.com/geofrocker/Yummy-Recipes/raw/master/A%20screen%20shot%20of%20flask%20running%20in%20cmd.png)
  * Visit your browser and enter `127.0.0.1/5000`
  * :boom::boom: You will be good to go


# How run test
  * Make sure all the requirements are installed by running `pip install -r requirements.txt`
  * Make sure you are in the projects root directory
  * Open your terminal and run `py.test test_app.py`
  * You will be good to go :boom::boom: