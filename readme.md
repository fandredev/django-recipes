## Stack used

<img src="https://skillicons.dev/icons?i=html,css,javascript,python,django,githubactions,selenium&theme=dark" />

**Tests:** Pytest, Unittest<br>
**Lint:** Ruff

## Authors

[@fandredev](https://www.linkedin.com/in/devfandre/)

## Installation with uv:

### First, clone this repository.

```bash
git clone git@github.com:fandredev/django-recipes.git
```

## Install dependencies and create environment

```bash
uv sync
```

## Run migrations to database

```bash
uv run python manage.py migrate
```

## Create a superuser

```bash
uv run python manage.py createsuperuser
```

## Clone the .env.example to .env before run server

```bash
cp .env.example .env
```

## Run development server

```bash
uv run python manage.py runserver
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
uv run python manage.py test
```

## Run ALL tests with pytest

```bash
uv run pytest
```

## Run functional tests with Selenium

```bash
uv run pytest -m 'functional'
```

## Run coverage with pytest

```bash
uv run coverage run -m pytest
```

## Open coverage report

```bash
uv run coverage html
```

<h4>After that, open the htmlcov folder and look for the index.html file.
Open it in your browser and the project coverage will be there</h4>
<br>

## Use collection

<h4>Use DRF.postman_collection.json file to use Django Rest Framework routes</h4>

![image](https://github.com/fandredev/django-recipes/assets/49297012/53ff7ffb-8810-4e39-8316-980c7a342a0d)

<br>

## Feedback

If you have any feedback, please let us know via profissionalf.andre@gmail.com

## Referencies

- [Django documentation](https://docs.djangoproject.com/en/5.0/)
- [Python](https://www.python.org/)
- [Django course by Otávio Miranda](https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/)
- [Pytest](https://docs.pytest.org/)
- [Unittest](https://docs.python.org/3/library/unittest.html)
- [Ruff](https://docs.astral.sh/ruff/)
- [Selenium](https://selenium.dev/)
