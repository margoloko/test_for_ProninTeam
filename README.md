#### test_for_ProninTeam
#### Тестовое задание Backend Python (ProninTeam)
![example workflow](https://github.com/margoloko/test_for_ProninTeam/blob/main/.github/workflow/workflow.yaml/badge.svg)

![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-5.0-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)

### Оглавление:
- [О проекте:](#о-проекте)
  - [Bеб-сервис на базе Django, предоставляющий CRUD REST API для групповых денежных сборов.](#bеб-сервис-на-базе-django-предоставляющий-crud-rest-api-для-групповых-денежных-сборов)
- [Запуск приложения](#запуск-приложения)

## О проекте:
### Bеб-сервис на базе Django, предоставляющий CRUD REST API для групповых денежных сборов.

1. Данные хранятся в реляционной БД, взаимодействие с ней осуществляется посредством Django ORM.
2. API реализовано на базе Django REST Framework.
3. Реализовано кэширование данных, возвращаемых GET-эндпоинтом, с обеспечением достоверности ответов.
4. Проект докеризирован и запускается через docker compose up .
5. Добавлена Management command для наполнения БД моковыми данными.

## Запуск приложения
**Клонирование реппозитория**

```sh
git clone git@github.com:margoloko/test_for_ProninTeam.git
```

Перейдите в папку с проектом **test_for_ProninTeam**, установите и запустите виртуальное окружение.

```sh
python -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```
