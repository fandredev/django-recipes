

## Autores

- [@fandredev](https://www.linkedin.com/in/devfandre/)


## Instalação

Clone o repositório
```bash
git clone git@github.com:fandredev/django-recipes.git
```

### Crie o ambiente virtual com o python:

```bash
python -m venv venv
```
### OU
```bash
python3 -m venv venv
```

### Ative o ambiente virtual:

```bash
source venv/bin/activate
```

### Instale as dependencias usando pip:
```bash
pip install -r requirements.txt
```

### Rode as migrations para o banco de dados:
```bash
python manage.py migrate
```
    
### Rode o servidor de desenvolvimento
```bash
python manage.py runserver
```

### Abra o servidor de desenvolvimento
```bash
Abra o browser e coloque http://127.0.0.1:8000/ na url do seu navegador.
```

### Abra o Django Admin
```bash
Abra o browser e coloque http://127.0.0.1:8000/admin na URL do seu navegador.
```
### Run tests
```bash
  python manage.py test
```

### Run coverage with pytest
```bash
coverage run -m pytest
```

### Open coverage cover in HTML file
```bash
coverage html
```
  Depois disso, abra a pasta htmlcov e procure o arquivo index.html. 
  Abra ele no seu navegador e lá estará a cobertura do projeto

## Stack utilizada

**Front-end:** HTML, CSS (in Templates)

**Back-end:** Django, Python

**Tests:** Pytest, Unittest

**CI/CD:** GH Actions


## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de profissionalf.andre@gmail.com

## Referência

 - [Django documentation](https://docs.djangoproject.com/en/5.0/)
 - [Python](https://www.python.org/)
 - [Django course by Otávio Miranda](https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/)
 - [Pytest](https://docs.pytest.org/)
 - [Unittest](https://docs.python.org/3/library/unittest.html)
