# nextstep

### clone this repo
``` git clone git@github.com:rodrigoddc/nextstep.git ```

### add .env file with config keys in, ex:

``` 
SECRET_KEY='some-super-scret-key'
ALLOWED_HOSTS=127.0.0.1, localhost
DEBUG=True
DATABASE_URL=postgres://DATABASE_USER:PASSWORD@localhost:5432/DATABASE_DB
```

### install pipenv
``` pip install pipenv ```

### install requirements
``` pipenv sync ```

### migrate models
``` python manage.py migrate ```

### run project
``` python manage.py runserver ```

