# For a living Project
## This repo will house the website (Django app) for the "For a Living" project

### Please following the following directions to set up your environment.

* We strongly recommend that you run this inside of a python virtual environment. 
  * More info on what a virtual environment and how to run it can be found [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

#### Please make sure that your virtual environment is activated before continuing (if you choose to go that route).

You should note that most (if not all) the dependencies will be installed from pip
* Next, since this is a Django application we will need to install Django
  * It can be downloaded with the following command: `pip install django`
  * You can check to see which version of Django you are running inside the python shell:
    * `import django`
    * `django.VERSION`

* We are currently using Postgres as our DB of choice. But for your convenience the lines of codes required to run sqlite were simply commented out (in foraliving_project/settings.py). Should you decide to use the latter of the two, simply swap out which DB info is commented out.
  * [Django girls](https://djangogirls.org/) provides a great documentation on [how](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/) to get Postgres running along side Django
  * Please remember to update the foraliving_project/settings.py DB section to reflect the credentials that you set up for your DB.

* The following are just other dependencies that are **required** to run the successfully run the project:
  * `pip install django-user-accounts`
  * `pip install pinax-theme-bootstrap`
  * `pip install metron`
  * `pip install BeautifulSoup`

##### If everything worked well, you should now be ready to run the project on your local machine.
  * To start the server, run `python manage.py runserver`
  * The default port is the infamous `8000` but you can specify another
    * Example: `python manage.py runserver 8080`
  