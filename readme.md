## Stack used

<img src="https://skillicons.dev/icons?i=html,css,javascript,python,django,githubactions,selenium&theme=dark" />

**Tests:** Pytest, Unittest<br>
**Lint:** Black



## Authors
[@fandredev](https://www.linkedin.com/in/devfandre/)


## Installation:
### First, clone this repository.
```bash
git clone git@github.com:fandredev/django-recipes.git
```

## Create virtual environment with Python

```bash
python -m venv venv
```
## OR
```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install dependencies using pip
```bash
pip install -r requirements.txt
```

## Run migrations to database
```bash
python manage.py migrate
```

## Create a superuser
```bash
python manage.py createsuperuser
```
    
## Run development server
```bash
python manage.py runserver
```

## Open development server
<h4>
Open browser and put http://127.0.0.1:8000/ in URL browser.
</h4>
<br>

## Open Django Admin
<h4>
In another tab, open browser and put http://127.0.0.1:8000/admin in URL browser. Log in with your superuser</h4>
<br>

## Run tests with unittest
```bash
python manage.py test
```

## Run ALL tests with pytest

``` 
pytest
``` 

## Run tests functionals with Selenium

```
pytest -m 'functional'
``` 

## Run coverage with pytest
```bash
coverage run -m pytest
```

## Open coverage cover in HTML file
```bash
coverage html
```
<h4>After that, open the htmlcov folder and look for the index.html file.
Open it in your browser and the project coverage will be there</h4>
<br>

# Use collection
<h4>Use DRF.postman_collection.json file to use Django Rest Framework routes</h4>
<br>


## Feedback

If you have any feedback, please let us know via profissionalf.andre@gmail.com

## Referencies

 - [Django documentation](https://docs.djangoproject.com/en/5.0/)
 - [Python](https://www.python.org/)
 - [Django course by Otávio Miranda](https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/)
 - [Pytest](https://docs.pytest.org/)
 - [Unittest](https://docs.python.org/3/library/unittest.html)
 - [Black formatter](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)
 - [Selenium](https://selenium.dev/)
