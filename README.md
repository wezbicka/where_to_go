# where_to_go

## Куда пойти — Москва глазами Артёма

Cайт о самых интересных местах в Москве. Авторский проект Артёма.

[Демка сайта](http://derzkayabelka.pythonanywhere.com/)

### Запуск

Для корректной работы Вам необходим Python версии 3.10.2

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```sh
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта.
- `ALLOWED_HOSTS` — список доменов/хостов, на которых будет работать сайт. Подробнее в [документации Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

Пример:

```env
DEBUG=True
SECRET_KEY=1rr!a(+$-8sf(9+sc)a-k2q%cqswc39qto#ba%wjv!or75h0k3
ALLOWED_HOSTS=localhost,127.0.0.1,example.com,www.example.com
```

## Добавление новых локаций

Для добавления новых локаций можно использовать [панель администратора](https://wezhbicka.pythonanywhere.com/admin/) 
или использовать команду из терминала:
* Для загрузки локального JSON файла:
```bash
python manage.py load_place --path my_place.json
```

* Для загрузки JSON файла по внешней ссылке:
```bash
python manage.py load_place --url http://example.com/my_place.json
```

*Для загрузки мест пачкой используйте:*

```bash
python manage.py load_place --batch batch.json
```

### Формат JSON файла

Для корректной работы скрипта необходим следующий формат JSON файла:

```json
{
    "title": "Название места",
    "imgs": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
    ],
    "description_short": "Краткое описание места",
    "description_long": "Полное описание локации. Допускается использование html-разметки.",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
