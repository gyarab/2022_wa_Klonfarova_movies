# Webová aplikace vytvořena v rámci předmětu webových aplikací



## Spusť enviroment

```git bash
python -m venv venv
```


## Spusť enviroment

```git bash
source ./venv/Scripts/activate
```

## Nainstaluj položky y requirements

```Bash
pip install -r requirements.txt
```


## Běž do GAMDB

```Bash

cd ./gamdb
```



## Vytvoř migrace

```Bash
py -Xutf8 manage.py makemigrations
```
```Bash
py manage.py migrate
```

## Naplň databázi

```Bash
py -Xutf8 manage.py loaddata --format yaml ./fixtures/*.yaml
```



## Spusť server

```Bash
py manage.py runserver
```
