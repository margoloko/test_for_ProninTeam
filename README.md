# test_for_ProninTeam
Тестовое задание Backend Python (ProninTeam)
![example workflow](https://github.com/margoloko/test_for_ProninTeam/actions/workflows/workflow.yaml/badge.svg)
![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-5.0-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)

Bеб-сервис на базе Django, предоставляющий CRUD REST API
для групповых денежных сборов.

Требования
1. Данные хранятся в реляционной БД, взаимодействие с ней
осуществляется посредством Django ORM.
2. API реализовано на базе Django REST Framework
3. Реализовано кэширование данных, возвращаемых GET-эндпоинтом, с
обеспечением достоверности ответов
4. Проект должен быть докеризирован и запускаться через docker compose up .
5. Должна присутствовать Management command для наполнения БД
моковыми данными (несколько тысяч).
