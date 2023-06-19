# scrap_wildberries
Парсит все товары искомого бренда с сайта https://www.wildberries.ru/. Сохраняет поля: 'id', 'название', 'цена', 'бренд', 'скидка', 'рейтинг', 'id продаца' в csv файл.

## Установка

Для работы требуется Python 3.9+. Скопируйте проект и установите зависимости:

```bash
  pip install -r requirements.txt
```

## Запуск

Запустите parser.py или вызовите ScrapWB('https://www.wildberries.ru/brands/название_бренда').parse() 

Замените на любой искомый бренд
