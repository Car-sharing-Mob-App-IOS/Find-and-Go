# Find and GO Backend
***
### Описание проекта
**Find and Go** - это бэкенд-приложение, разработанное выпускниками **Яндекс Практикума** под руководством наставников. Проект, созданный на основе Django и Django Rest Framework (DRF), призван обеспечить функциональность iOS-приложения. **Find and Go** является агрегатором каршеринга, предоставляя пользователям удобный доступ к множеству машин от различных компаний.
***

### Функциональности
**Регистрация и управление пользователями**
- ***Регистрация пользователя***: Пользователи могут зарегистрироваться, предоставив необходимую информацию.
- ***Сброс пароля через электронную почту***: Пользователи могут восстановить свой пароль, получив инструкции на электронную почту.
- ***Редактирование и удаление пользователя:*** Авторизованные пользователи имеют возможность изменять свой профиль и удалять свою учетную запись.

**Оценки и отзывы**
- ***Оценки и отзывы для машин:*** Пользователи могут оценивать и оставлять отзывы для машин, выражая свое мнение о предоставляемых услугах.

**Фильтры**
- ***Фильтр по названию компании каршеринга:*** Позволяет пользователям легко находить машины, предоставляемые определенной компанией каршеринга.
- ***Фильтр по уникальному слагу:*** Обеспечивает возможность поиска машин по уникальному слагу, включая дополнительные опции, такие как детское кресло, подогрев руля и другие.
- ***Фильтр по модели машины:*** Позволяет пользователям выбирать машины определенной модели.
- ***Фильтр по запасу хода:*** Пользователи могут ограничивать выбор машин в зависимости от необходимого им запаса хода.
- ***Фильтр по типу двигателя:*** Позволяет пользователям фильтровать машины по типу используемого двигателя.
- ***Фильтр по координатам:*** Обеспечивает возможность поиска машин в определенной географической области.
- ***Фильтр по типу автомобиля:*** Позволяет пользователям выбирать машины определенного типа, такие как купе, седан, хэтчбек и другие.

Эти фильтры предоставляют пользователям гибкость в поиске и выборе машин, отвечающих их конкретным потребностям и предпочтениям.

**Ранжирование машин**
- ***Ранжирование машин по координатам:*** Если пользователь авторизован и запрашивает список машин, то машины ранжируются от наиболее близкой до самой дальней на основе координат.

**Аутентификация**

- ```POST /auth/o/yandex/:``` Аутентификация через Яндекс.
- ```POST /auth/o/mail/: ``` Аутентификация через Mail.
- ```POST /auth/token/login: ``` Аутентификация по токену.

<details>
 <summary> Технологии </summary>
  
  - Python 3.10
  - Django 3.2.3
  - Django REST framework 3.12.4
  - Docker
  - Django
  - django-filter
  - django-oauth-toolkit
  - django-rest-framework-social-oauth2
  - django-rest-swagger
  - djangorestframework
  - djangorestframework-simplejwt
  - djoser
  - drf-spectacular
  - gunicorn
  - Pillow
  - requests
  - nginx
  - CI/CD
</details>

<details>
 <summary> Инструкции по установке </summary>
 <details>
     <summary> Локально </summary>
     
    1. Клонируйте репозиторий: ``git clone git@github.com:VlKazmin/car-hub.git``
    2. Перейдите в директорию проекта: ```cd find-and-go/backend```
    3. Установите зависимости: ```pip install -r requirements.txt```
    4. Примените миграции: ```python manage.py migrate```
    5. Загрузите фикстуры:``` python manage.py load_fixtures```
    6. Запустите сервер: ```python manage.py runserver```
  
   </details>

  <details>
 <summary> Docker </summary>
 
     **Склонируйте репозиторий и настройте окружение:**
  ```bash
      git clone git@github.com:VlKazmin/Find-and-Go.git
      cd find-and-go/
      # сделайте копию файла <.env.template> в <.env>
      cp -i .env.template .env
  ```
     **Запустите приложение с помощью Docker:**
  ```bash
      sudo docker compose -f docker-compose.production.yml up --build -d
      sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations
      sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
      sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
      sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
      # Для заполнения базы ингредиентами выполните:
      sudo docker compose -f docker-compose.production.yml exec backend python manage.py load_fixtures
      # Для создания суперпользователя
      sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
  ```
  ***
  **Проект будет доступен по адресу -  http://localhost:8000/**
  **Документация будет доступен по адресу -  http://localhost:8000/api/v1/swagger/**
  ***
   </details>

 </details>

## Ссылки
Дизайн в Figma - [посмотреть](https://www.figma.com/file/ubkBwKt1JpNrIhYzWHJdNv/Агрегатор-каршеринга?type=design&node-id=730-9413&mode=design&t=TM5epAcWfBOYRtnw-0)


## Изображения
<img width="260" alt="carsharing1" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/809a3896-e0e3-42f6-8e3b-bb968f66d005">  
<img width="260" alt="carsharing2" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/ffa83a4a-91d6-4ae5-929e-276f48dfe50e">
<img width="260" alt="carsharing3" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/b035c2be-a86e-42e7-97a4-d9614fe1df8f">
<img width="260" alt="carsharing4" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/c1cdfbf4-b1a8-44a9-8c1e-1bc1e1c7d646">
<img width="260" alt="carsharing5" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/b055919e-5dfc-4ae1-aaec-10fcbc695582">
<img width="260" alt="carsharing6" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/6e2a73ad-9718-4c8a-9d9c-ef435f96ddcd">
<img width="260" alt="carsharing7" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/1353f0ff-ef31-4f61-b885-5f55247baf5f">
<img width="260" alt="carsharing8" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/653f7613-cbd9-4347-8cf8-52dfa467f2f9">
<img width="260" alt="carsharing9" src="https://github.com/Mobile-App-Carsharing-Aggregator/ios-rep/assets/110411999/c26158e2-29a6-4120-9aaf-5916467fc57f">

## Авторы

***backend:***

- **Владислав Казьмин** - [GitHub](https://github.com/vlkazmin)
- **Марат Шайбаков** - [GitHub](https://github.com/smaspb17)
- **Данил Воронин** - [GitHub](https://github.com/Bogdan-Malina)
- **Никита Нестеренко** - [GitHub](https://github.com/nikitairl) 
- **Ольга** - [GitHub](https://github.com/OlgaSHp)  
 
 





