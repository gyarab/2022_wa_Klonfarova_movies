# 2022_wa_Klonfarova_movies


## Spustit enviroment

```git bash
source ./venv/Scripts/activate
```

## Nainstalovat polozky y requirements

```Bash
pip install -r requirements.txt
```

## Spustit server

```Bash
python manage.py runserver
```

## Vytvor fixtures

```Bash
python manage.py dumpdata <app_model_name> --format yaml > fixtures/<name>.yaml
```
## Naloaduj fixtures

```Bash
python manage.py loaddata fixtures/<name>.yaml --app <app_model_name>
```
