

## Authors

- [@fandredev](https://www.linkedin.com/in/devfandre/)


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
    
## Run development server
```bash
python manage.py runserver
```

## Open development server
```bash
Abra o browser e coloque http://127.0.0.1:8000/ na url do seu navegador.
```

## Open Django Admin
```bash
Abra o browser e coloque http://127.0.0.1:8000/admin na URL do seu navegador.
```
## Run tests
```bash
python manage.py test
```

## Run coverage with pytest
```bash
coverage run -m pytest
```

## Open coverage cover in HTML file
```bash
coverage html
```
After that, open the htmlcov folder and look for the index.html file.
Open it in your browser and the project coverage will be there

## Stack used

**Front-end:** HTML, CSS (in Templates)

**Back-end:** Django, Python

**Tests:** Pytest, Unittest

**CI/CD:** GH Actions

**Lint:** Black


## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de profissionalf.andre@gmail.com

## Referencies

 - [Django documentation](https://docs.djangoproject.com/en/5.0/)
 - [Python](https://www.python.org/)
 - [Django course by Otávio Miranda](https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/)
 - [Pytest](https://docs.pytest.org/)
 - [Unittest](https://docs.python.org/3/library/unittest.html)
 - [Black formatter](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)
