### REST API для проекта YATUBE:
---

Проект Yatube - это социальная сеть для публикации личных дневников.
Зарегистрированный пользователь может создавать публикации, подписываться на авторов и комментировать из записи, а также изменять и удалять свои публикации и комментарии. Есть возможность присоединять записи к сообществу.

Для незарегистрированного пользователя доступен просмотр публикаций и комментариев, а также информация о сообществах.

При создании API использована библиотека Django REST framework. Передача данных осуществляется в формате JSON.

#### 1. Как запустить проект:
---
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Olkhovik-mv/api_final_yatube.git
```
```
cd api_final_yatube
```
- Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source env/bin/activate
```
- Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python3 manage.py migrate
```
- Запустить проект:
```
python3 manage.py runserver
```
#### 2. Регистрация пользователя
---
Регистрация пользователя через API техническим заданием не предусмотрена, и возможно, будет реализована в следующих версиях. В настоящий момент зарегистрировать пользователя можно через админку по адресу `/admin/`. Для входа в админку необходимо создать суперпользователя, для этого после запуска проекта в коммандной строке ввести: 
```bash
python manage.py createsuperuser
```

#### 3. Получение токена
---
Контроль пользователей в API реализован по JWT - токену. 
Для получения токена нужно отправить POST запрос на эндпоинт `/api/v1/jwt/create/`
```JSON
{
	"username": "newuser",
	"password": "Changeme"
}
```

#### 4. Документация
---
После запуска проекта документация к API доступна по  адресу `/redoc/`.
![Документация к api](/readme_assets/redoc.jpg)
#### 5. Передача изображений
---
При публикации и редактировании поста есть возможность прикрепить изображение. Для этого необходимо преобразовать изображение в текст, используя Base64. Полученную текстовую строку вставить в поле `image`.
#### 6. Сообщества
---
Присоединение публикации к сообществу происходит при указании id сообщества в поле `group`  публикации. При этом существующие группы доступны по адресу
```
/api/v1/groups/
```
Добавление новых сообществ через API не реализовано и доступно через админку.