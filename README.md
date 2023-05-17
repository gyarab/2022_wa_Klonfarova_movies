# Webová aplikace vytvořena v rámci předmětu webových aplikací


## Spusť enviroment

```git bash
source ./venv/Scripts/activate
```

## Nainstaluj položky y requirements

```Bash
pip install -r requirements.txt
```

## Spusť server

```Bash
python manage.py runserver
```

## Vytvoř fixtures

```Bash
python manage.py dumpdata <app_model_name> --format yaml > fixtures/<name>.yaml
```
## Naloaduj fixtures

```Bash
python manage.py loaddata fixtures/<name>.yaml --app <app_model_name>
```
