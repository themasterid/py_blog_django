# Описание
### YaTube представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Технологии
Python 3.7, Django 3.2, DRF, JWT + Joser

Технологии:
- Django 3.2
- Bootstrap 5
- HTML
- CSS
- JS
- CKEDITOR

### Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке.
Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
```
$ py -3.7 -m venv venv
$ venv/Scripts/activate
$ python -m pip install --upgrade pip
```
Затем нужно установить все зависимости из файла requirements.txt
```
$ pip install -r requirements.txt
```
Выполняем миграции:
```
$ python manage.py migrate
```
TODO - дописать.
