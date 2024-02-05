# GUIDELINE from me and for, Django benginer

> A command **django-admin help** will show each command

1. Make Django connector app: 
```shell
$ python -m django-admin startproject [project name]
# Or 
$ python manage.py startproject
```
* **manage.py** does same things as well as **django-admin**
2. Make my Django App:
```bash
$ python manage.py
```
2. Make new sepearated app for my own purposes:
```bash
$ python manage.py startapp [application_name]
```
3. Run server using built-in command
```bash
$ python mange.py runserver
```

## How to change default database SQL lite?
Of course is possible, change must applied in settings.py from _connector app_ under key "**DATABASES**"

## Prerequsites
1. View function always take as parameter request. Otherwise always error will be throw. Nevertheless its good habit
