# parser-categories
парсер для партньоров luxel.ua
python=3
```
pip install requests bs4
```

у файде config.py добавляєм список силок нужних нам категорий
```
LUXEL_CATEGORIES=[
...
]#список силок нужних нам категорий
LUXEL_RESULT_FILE = "*.csv"# файл с результатом 
```
запуск скрипта

```
python manage.py
```
