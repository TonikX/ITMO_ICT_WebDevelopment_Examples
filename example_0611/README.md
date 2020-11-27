### Имплементация MKdocs

## Установка Mkdocs

```python pip install mkdocs```

## Старт

```mkdocs new app-example``` - генерируем проект
```mkdocs serve``` - запускаем
Переходим на ```http://127.0.0.1:8000/```

## Добавление новой страницы
Добавим в mkdocs.yml тег nav с ассоциацией роутинга с файлом md.
```
site_name: My Docs
nav:
    - Home: index.md
    - About: about.md
```

После обновление конфигурационного файла создадим файл docs/about.md c произвольным значением.
Перезапускаем сервер и переходим по ```http://127.0.0.1:8000/about/``` и видим содержание about.md 

