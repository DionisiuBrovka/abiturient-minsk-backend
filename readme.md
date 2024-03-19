# Бэкенд приложение "Абитуриент МИНСК"

## Полезности

### Запуск на проде (докер)

 - ``` docker-compose down -v ``` (На всякий слуйчай выключаем заранее созданный стек контейнеров)
 - ``` docker-compose build ``` (Собираем изображения контайнеров)
 - ``` docker-compose up -d ``` (Запускаем стек контейнеров)
 - ``` docker-compose exec api python manage.py migrate ``` (Применяем миграции для проекта)

### Другие действия:
Сделать дамп данных :
 - ``` docker exec -t -i <контейнер> sh ``` (Заходим в терминал контейнера)
 - ``` python -Xutf8 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json ``` (Делаем дамп данных)
 - ``` exit ``` (выходим из контейнера)
 - ``` docker cp <контейнер>:/code/db.json . ``` (копируем дамп из контейнера)
 